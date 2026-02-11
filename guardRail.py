from .Variables import *
from .gameController import gameController
from .gameHandler import gameHandler
from .Tools import *

class GuardRail:
	def __init__(self, memory_controller: gameController, game_handler: gameHandler, options: dict):
		self.memory_controller = memory_controller
		self.pm = memory_controller.pm
		self.game_handler = game_handler
		self.options = options

	def check_memory_addresses(self):
		result = {"error": False, "message": ""}

		# We check if the the sound hack has been applied correctly
		start_sound_hack_1 = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrSoundHack1, 2))
		start_sound_hack_2 = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrSoundHack2, 2))

		if start_sound_hack_1 != 0x6A00 or start_sound_hack_2 != 0xE91A:
			result["error"] = True
			result["message"] = "Sound Hack not applied correctly."

		if not result["error"]:
			# We check if the practice starting lives has been set correctly
			practice_starting_lives = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrPracticeStartingLives, 1))
			if practice_starting_lives != self.game_handler.getLives():
				result["error"] = True
				result["message"] = f"Practice starting lives not set correctly. Game: {practice_starting_lives}, Expected: {self.game_handler.getLives()}"

		if not result["error"]:
			# We check if the normal starting lives has been set correctly
			normal_starting_lives = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrNormalStartingLives, 1))
			if normal_starting_lives != self.game_handler.getLives():
				result["error"] = True
				result["message"] = f"Normal starting lives not set correctly. Game: {normal_starting_lives}, Expected: {self.game_handler.getLives()}"

		if not result["error"]:
			# We check if the Extra/Phantasm starting lives has been set correctly
			extra_starting_lives = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrExtraPhantasmStartingLives, 1))
			if extra_starting_lives != self.game_handler.getLives():
				result["error"] = True
				result["message"] = f"Extra/Phantasm starting lives not set correctly. Game: {extra_starting_lives}, Expected: {self.game_handler.getLives()}"

		if not result["error"]:
			# We check if the lives after a continue has been set correctly
			lives_after_continue = int.from_bytes(self.pm.read_bytes(self.memory_controller.addrNormalContinueLives, 1))
			if lives_after_continue != self.game_handler.getLives():
				result["error"] = True
				result["message"] = f"Lives after continue not set correctly. Game: {lives_after_continue}, Expected: {self.game_handler.getLives()}"

		if not result["error"]:
			# We check if the starting bombs has been set correctly
			starting_bombs = self.pm.read_float(self.memory_controller.addrStartingBombs)
			if starting_bombs != self.game_handler.getBombs():
				result["error"] = True
				result["message"] = f"Starting bombs not set correctly. Game: {starting_bombs}, Expected: {self.game_handler.getBombs()}"

		if not result["error"]:
			# We check if the starting power points has been set correctly
			starting_power_points = self.pm.read_float(self.memory_controller.addrStartingPowerPoint)
			if starting_power_points != self.game_handler.getPower():
				result["error"] = True
				result["message"] = f"Starting power points not set correctly. Game: {starting_power_points}, Expected: {self.game_handler.getPower()}"

		return result

	def check_cursor_state(self):
		result = {"error": False, "message": ""}

		# If we're in the menu
		if self.game_handler.getGameMode() != IN_GAME:
			menu = self.game_handler.getMenu()
			cursor = self.memory_controller.getMenuCursor()
			if menu >= 0 and cursor < 50:
				# If we're in the character select, we check if the cursor is on a character that is unlocked
				if menu in [NORMAL_CHARACTER_MENU, PRACTICE_CHARACTER_MENU, EXTRA_CHARACTER_MENU]:
					characters = self.game_handler.characters
					if not characters[cursor][SHOT_A] and not characters[cursor][SHOT_B]:
						result["error"] = True
						result["message"] = f"Character {cursor} is locked."
				# If we're in the shot type select, we check if the cursor is on a shot type that is unlocked
				if menu in [NORMAL_SHOT_TYPE_MENU, PRACTICE_SHOT_TYPE_MENU, EXTRA_SHOT_TYPE_MENU]:
					characters = self.game_handler.characters
					currentCharacter = self.memory_controller.getCharacter()
					if not characters[currentCharacter][cursor]:
						result["error"] = True
						result["message"] = f"Shot Type {cursor} is locked."
				# If we're in the difficulty select, we check if the cursor is on a difficulty that is unlocked
				elif menu in [NORMAL_DIFFICULTY_MENU, PRACTICE_DIFFICULTY_MENU]:
					lowest_difficulty = self.game_handler.getLowestDifficulty()
					if cursor < lowest_difficulty:
						result["error"] = True
						result["message"] = f"Difficulty {cursor} is locked."
				# If we're in the stage select screen, we check if the cursor is on a stage that is unlocked
				elif menu == PRACTICE_STAGE_SELECT_MENU:
					characters = self.memory_controller.getCharacter()
					shot_type = self.memory_controller.getShotType()
					stages = self.game_handler.stages[characters][shot_type]
					if stages <= cursor:
						result["error"] = True
						result["message"] = f"Stage {cursor} is locked."

		return result

	def check_menu_lock(self):
		result = {"error": False, "message": ""}

		# If we're in the menu
		if self.game_handler.getGameMode() != IN_GAME:
			menu = self.game_handler.getMenu()
			if menu >= 0:
				# If we're in the difficulty select, we check if the difficulties are locked correctly
				if menu in [NORMAL_DIFFICULTY_MENU, PRACTICE_DIFFICULTY_MENU]:
					lock_down = self.memory_controller.getDifficultyDown()
					lock_up = self.memory_controller.getDifficultyUp()
					lowest_difficulty = self.game_handler.getLowestDifficulty()
					if lock_down != lowest_difficulty or lock_up != lowest_difficulty:
						result["error"] = True
						result["message"] = f"Difficulty locks are not set correctly."
				# If we're in the character select, we check if the character list is correct
				elif menu in [NORMAL_CHARACTER_MENU, PRACTICE_CHARACTER_MENU, EXTRA_CHARACTER_MENU]:
					for character in CHARACTERS:
						for shot in SHOTS:
							characterExtraAccess = self.memory_controller.getCharacterDifficulty(character, shot, EXTRA)
							characterUnlocked = True if characterExtraAccess == 99 else False
							characterLogicallyUnlocked = self.game_handler.characters[character][shot]
							characterHasExtra = self.game_handler.characters[character][shot] and self.game_handler.hasExtra[character][shot]
							characterHasPhantasm = self.game_handler.characters[character][shot] and self.game_handler.hasPhantasm[character][shot]
							difficulty = self.memory_controller.getDifficulty()

							if menu == EXTRA_CHARACTER_MENU:
								if difficulty == EXTRA and characterUnlocked != characterHasExtra:
									result["error"] = True
									result["message"] = f"Character {character} Extra access is not locked or unlocked correctly. Extra Logical state: {characterLogicallyUnlocked}. Current state: {characterHasExtra}."

								if difficulty == PHANTASM and characterUnlocked != characterHasPhantasm:
									result["error"] = True
									result["message"] = f"Character {character} Phantasm access is not locked or unlocked correctly. Phantasm Logical state: {characterLogicallyUnlocked}. Current state: {characterHasPhantasm}."
							else:
								if characterUnlocked != characterLogicallyUnlocked:
									result["error"] = True
									result["message"] = f"Character {character} is not locked or unlocked correctly. Logical state: {characterLogicallyUnlocked}. Current state: {characterUnlocked}."
				# If we're in the main menu, we check if the extra stage and normal mode are locked or unlocked correctly
				elif menu == MAIN_MENU:
					can_extra = self.game_handler.canExtra()
					can_phantasm = self.game_handler.canPhantasm()
					lock_down = self.memory_controller.getDifficultyDown()
					lock_up = self.memory_controller.getDifficultyUp()
					minimum_cursor = 0 if self.options['mode'] in NORMAL_MODE else 1

					if not can_extra and not can_phantasm and self.options['mode'] not in NORMAL_MODE:
						minimum_cursor += 1

					if lock_down != minimum_cursor or lock_up != minimum_cursor:
						result["error"] = True
						result["message"] = f"Main menu cursor is not locked correctly. Minimum cursor should be {minimum_cursor}. Current locks are: {lock_down}, {lock_up}."

			if not result["error"]:
				# We check if stages are unlocked correctly if we're in practice mode
				if self.options["mode"] == PRACTICE_MODE:
					stages = self.game_handler.stages
					for character in CHARACTERS:
						for shot in SHOTS:
							handler_stage = stages[character][shot]
							for difficulty in range(4):
								if self.game_handler.characters[character][shot] and difficulty >= self.game_handler.getLowestDifficulty():
									in_game_stage = self.memory_controller.getCharacterDifficulty(character, shot, difficulty)

									if in_game_stage != handler_stage:
										result["error"] = True
										result["message"] = f"Character {character} - {shot} has incorrect stages ({in_game_stage} != {handler_stage}) for difficulty {difficulty}."

		return result