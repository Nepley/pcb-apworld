import pymem
import pymem.exception
from .Tools import getPointerAddress
from .Variables import *

class gameController:
	"""Class accessing the game memory"""

	def __init__(self):
		self.pm = pymem.Pymem(GAME_NAME)

		self.addrStage = self.pm.base_address+ADDR_STAGE
		self.addrDifficulty = self.pm.base_address+ADDR_DIFFICULTY
		self.addrRank = self.pm.base_address+ADDR_RANK
		self.addrCharacter = self.pm.base_address+ADDR_CHARACTER
		self.addrShotType = self.pm.base_address+ADDR_SHOT_TYPE

		self.addrLives = getPointerAddress(self.pm, self.pm.base_address+ADDR_LIVES[0], ADDR_LIVES[1:])
		self.addrBombs = getPointerAddress(self.pm, self.pm.base_address+ADDR_BOMBS[0], ADDR_BOMBS[1:])
		self.addrPower = getPointerAddress(self.pm, self.pm.base_address+ADDR_POWER[0], ADDR_POWER[1:])
		self.addrContinues = getPointerAddress(self.pm, self.pm.base_address+ADDR_CONTINUE[0], ADDR_CONTINUE[1:])

		self.addrNormalStartingLives = self.pm.base_address+ADDR_NORMAL_STARTING_LIVES
		self.addrNormalContinueLives = self.pm.base_address+ADDR_NORMAL_CONTINUE_LIVES
		self.addrPracticeStartingLives = self.pm.base_address+ADDR_PRACTICE_STARTING_LIVES
		self.addrExtraPhantasmStartingLives = self.pm.base_address+ADDR_EXTRA_PHANTASM_STARTING_LIVES
		self.addrStartingBombs = self.pm.base_address+ADDR_STARTING_BOMBS
		self.addrStartingPowerPoint = self.pm.base_address+ADDR_STARTING_POWER_POINT

		self.addrBaseCherry = getPointerAddress(self.pm, self.pm.base_address+ADDR_BASE_CHERRY[0], ADDR_BASE_CHERRY[1:])
		self.addrCherry = self.pm.base_address+ADDR_CHERRY
		self.addrCherryPlus = self.pm.base_address+ADDR_CHERRY_PLUS
		self.addrCherryPlusMax = self.pm.base_address+ADDR_CHERRY_PLUS_MAX
		self.addrCherryGiveLine = self.pm.base_address+ADDR_CHERRY_GIVE_LINE
		self.addrCherryPlusGiveLine = self.pm.base_address+ADDR_CHERRY_PLUS_GIVE_LINE

		self.addrMisses = getPointerAddress(self.pm, self.pm.base_address+ADDR_MISSES[0], ADDR_MISSES[1:])
		self.addrScore = getPointerAddress(self.pm, self.pm.base_address+ADDR_SCORE[0], ADDR_SCORE[1:])

		self.addrReimuAEasy = self.pm.base_address+ADDR_REIMU_A_EASY
		self.addrReimuANormal = self.pm.base_address+ADDR_REIMU_A_NORMAL
		self.addrReimuAHard = self.pm.base_address+ADDR_REIMU_A_HARD
		self.addrReimuALunatic = self.pm.base_address+ADDR_REIMU_A_LUNATIC

		self.addrReimuBEasy = self.pm.base_address+ADDR_REIMU_B_EASY
		self.addrReimuBNormal = self.pm.base_address+ADDR_REIMU_B_NORMAL
		self.addrReimuBHard = self.pm.base_address+ADDR_REIMU_B_HARD
		self.addrReimuBLunatic = self.pm.base_address+ADDR_REIMU_B_LUNATIC

		self.addrMarisaAEasy = self.pm.base_address+ADDR_MARISA_A_EASY
		self.addrMarisaANormal = self.pm.base_address+ADDR_MARISA_A_NORMAL
		self.addrMarisaAHard = self.pm.base_address+ADDR_MARISA_A_HARD
		self.addrMarisaALunatic = self.pm.base_address+ADDR_MARISA_A_LUNATIC

		self.addrMarisaBEasy = self.pm.base_address+ADDR_MARISA_B_EASY
		self.addrMarisaBNormal = self.pm.base_address+ADDR_MARISA_B_NORMAL
		self.addrMarisaBHard = self.pm.base_address+ADDR_MARISA_B_HARD
		self.addrMarisaBLunatic = self.pm.base_address+ADDR_MARISA_B_LUNATIC

		self.addrSakuyaAEasy = self.pm.base_address+ADDR_SAKUYA_A_EASY
		self.addrSakuyaANormal = self.pm.base_address+ADDR_SAKUYA_A_NORMAL
		self.addrSakuyaAHard = self.pm.base_address+ADDR_SAKUYA_A_HARD
		self.addrSakuyaALunatic = self.pm.base_address+ADDR_SAKUYA_A_LUNATIC

		self.addrSakuyaBEasy = self.pm.base_address+ADDR_SAKUYA_B_EASY
		self.addrSakuyaBNormal = self.pm.base_address+ADDR_SAKUYA_B_NORMAL
		self.addrSakuyaBHard = self.pm.base_address+ADDR_SAKUYA_B_HARD
		self.addrSakuyaBLunatic = self.pm.base_address+ADDR_SAKUYA_B_LUNATIC

		self.addrReimuAExtra = self.pm.base_address+ADDR_REIMU_A_EXTRA
		self.addrReimuBExtra = self.pm.base_address+ADDR_REIMU_B_EXTRA
		self.addrMarisaAExtra = self.pm.base_address+ADDR_MARISA_A_EXTRA
		self.addrMarisaBExtra = self.pm.base_address+ADDR_MARISA_B_EXTRA
		self.addrSakuyaAExtra = self.pm.base_address+ADDR_SAKUYA_A_EXTRA
		self.addrSakuyaBExtra = self.pm.base_address+ADDR_SAKUYA_B_EXTRA

		self.addrReimuAPhantasm = self.pm.base_address+ADDR_REIMU_A_PHANTASM
		self.addrReimuBPhantasm = self.pm.base_address+ADDR_REIMU_B_PHANTASM
		self.addrMarisaAPhantasm = self.pm.base_address+ADDR_MARISA_A_PHANTASM
		self.addrMarisaBPhantasm = self.pm.base_address+ADDR_MARISA_B_PHANTASM
		self.addrSakuyaAPhantasm = self.pm.base_address+ADDR_SAKUYA_A_PHANTASM
		self.addrSakuyaBPhantasm = self.pm.base_address+ADDR_SAKUYA_B_PHANTASM

		self.addrControllerHandle = self.pm.base_address+ADDR_CONTROLLER_HANDLER
		self.addrInput = self.pm.base_address+ADDR_INPUT
		self.addrGameMode = self.pm.base_address+ADDR_GAME_MODE
		self.addrMenu = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU[0], ADDR_MENU[1:])
		self.addrMenuCursor =  getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU_CURSOR[0], ADDR_MENU_CURSOR[1:])
		self.addrIsBossPresent = self.pm.base_address+ADDR_IS_BOSS_PRESENT
		self.addrDemoCondtion = self.pm.base_address+ADDR_DEMO_CONDITION
		self.addrFocusCondition = self.pm.base_address+ADDR_FOCUS_CONDITION
		self.addrAntiTemperHack = self.pm.base_address+ADDR_ANTI_TEMPER_HACK

		self.addrKillCondition = self.pm.base_address+ADDR_KILL_CONDITION

		self.addrCharacterLock = [self.pm.base_address+ADDR_LOCK_1, self.pm.base_address+ADDR_LOCK_2, self.pm.base_address+ADDR_LOCK_3, self.pm.base_address+ADDR_LOCK_4]

		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])

		self.addrLifeHack1 = self.pm.base_address+ADDR_LIVES_HACK_1
		self.addrLifeHack2 = self.pm.base_address+ADDR_LIVES_HACK_2
		self.addrBombHack1 = self.pm.base_address+ADDR_BOMB_HACK_1
		self.addrBombHack2 = self.pm.base_address+ADDR_BOMB_HACK_2
		self.addrPowerHack1 = self.pm.base_address+ADDR_POWER_HACK_1
		self.addrPowerHack2 = self.pm.base_address+ADDR_POWER_HACK_2
		self.addrPowerHack3 = self.pm.base_address+ADDR_POWER_HACK_3

		self.addrCustomSoundId = self.pm.base_address+ADDR_CUSTOM_SOUND_ID
		self.addrSoundHack1 = self.pm.base_address+ADDR_SOUND_HACK_1
		self.addrSoundHack2 = self.pm.base_address+ADDR_SOUND_HACK_2

		self.addrFpsText = self.pm.base_address+ADDR_FPS_TEXT
		self.addrFpsUpdate = self.pm.base_address+ADDR_FPS_UPDATE

		self.addrDifficultyDown = self.pm.base_address+ADDR_DIFFICULTY_DOWN
		self.addrDifficultyUp = self.pm.base_address+ADDR_DIFFICULTY_UP
		self.addrDifficutlyCondition = self.pm.base_address+ADDR_DIFFICULTY_CONDITION
		self.addrLastDifficulty = self.pm.base_address+ADDR_LAST_DIFFICULTY
		self.addrDefaultDifficulty1 = self.pm.base_address+ADDR_DEFAULT_DIFFICULTY_1
		self.addrDefaultDifficulty2 = self.pm.base_address+ADDR_DEFAULT_DIFFICULTY_2
		self.addrDefaultExtraDifficulty = self.pm.base_address+ADDR_DEFAULT_EXTRA_DIFFICULTY

		self.addrTime1 = getPointerAddress(self.pm, self.pm.base_address+ADDR_TIME_1[0], ADDR_TIME_1[1:])
		self.addrTime2 = getPointerAddress(self.pm, self.pm.base_address+ADDR_TIME_2[0], ADDR_TIME_2[1:])

		self.addrPracticeScore = {
			REIMU:
				{
					SHOT_A:
					{
						EASY:
						[
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_6,
						],
					},
					SHOT_B:
					{
						EASY:
						[
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_6,
						],
					}

				},
			MARISA:
				{
					SHOT_A:
					{
						EASY:
						[
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_6,
						],
					},
					SHOT_B:
					{
						EASY:
						[
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_6,
						],
					}
				},
			SAKUYA:
				{
					SHOT_A:
					{
						EASY:
						[
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_A_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_A_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_A_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_A_LUNATIC_SCORE_6,
						],
					},
					SHOT_B:
					{
						EASY:
						[
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_B_EASY_SCORE_6,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_B_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_B_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_SAKUYA_B_LUNATIC_SCORE_6,
						],
					}
				}
		}

	def getStage(self):
		return int.from_bytes(self.pm.read_bytes(self.addrStage, 1))

	def getDifficulty(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficulty, 1))

	def getRank(self):
		return int.from_bytes(self.pm.read_bytes(self.addrRank, 1))

	def getCharacter(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCharacter, 1))

	def getShotType(self):
		return int.from_bytes(self.pm.read_bytes(self.addrShotType, 1))

	def getLives(self):
		self.addrLives = getPointerAddress(self.pm, self.pm.base_address+ADDR_LIVES[0], ADDR_LIVES[1:])
		return int(self.pm.read_float(self.addrLives))

	def getBombs(self):
		self.addrBombs = getPointerAddress(self.pm, self.pm.base_address+ADDR_BOMBS[0], ADDR_BOMBS[1:])
		return int(self.pm.read_float(self.addrBombs))

	def getPower(self):
		self.addrPower = getPointerAddress(self.pm, self.pm.base_address+ADDR_POWER[0], ADDR_POWER[1:])
		return int(self.pm.read_float(self.addrPower))

	def getMisses(self):
		self.addrMisses = getPointerAddress(self.pm, self.pm.base_address+ADDR_MISSES[0], ADDR_MISSES[1:])
		return int(self.pm.read_float(self.addrMisses))

	def getScore(self):
		self.addrScore = getPointerAddress(self.pm, self.pm.base_address+ADDR_SCORE[0], ADDR_SCORE[1:])
		return self.pm.read_int(self.addrScore)

	def getContinues(self):
		self.addrContinues = getPointerAddress(self.pm, self.pm.base_address+ADDR_CONTINUE[0], ADDR_CONTINUE[1:])
		return int.from_bytes(self.pm.read_bytes(self.addrContinues, 1))

	def getReimuAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAEasy, 1))

	def getReimuANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuANormal, 1))

	def getReimuAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAHard, 1))

	def getReimuALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuALunatic, 1))

	def getReimuAExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAExtra, 1))

	def getReimuAPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAPhantasm, 1))

	def getReimuBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBEasy, 1))

	def getReimuBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBNormal, 1))

	def getReimuBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBHard, 1))

	def getReimuBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBLunatic, 1))

	def getReimuBExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBExtra, 1))

	def getReimuBPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBPhantasm, 1))

	def getMarisaAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAEasy, 1))

	def getMarisaANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaANormal, 1))

	def getMarisaAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAHard, 1))

	def getMarisaALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaALunatic, 1))

	def getMarisaAExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAExtra, 1))

	def getMarisaAPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAPhantasm, 1))

	def getMarisaBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBEasy, 1))

	def getMarisaBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBNormal, 1))

	def getMarisaBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBHard, 1))

	def getMarisaBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBLunatic, 1))

	def getMarisaBExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBExtra, 1))

	def getMarisaBPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBPhantasm, 1))

	def getSakuyaAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaAEasy, 1))

	def getSakuyaANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaANormal, 1))

	def getSakuyaAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaAHard, 1))

	def getSakuyaALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaALunatic, 1))

	def getSakuyaAExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaAExtra, 1))

	def getSakuyaAPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaAPhantasm, 1))

	def getSakuyaBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBEasy, 1))

	def getSakuyaBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBNormal, 1))

	def getSakuyaBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBHard, 1))

	def getSakuyaBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBLunatic, 1))

	def getSakuyaBExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBExtra, 1))

	def getSakuyaBPhantasm(self):
		return int.from_bytes(self.pm.read_bytes(self.addrSakuyaBPhantasm, 1))

	def getInput(self):
		return int.from_bytes(self.pm.read_bytes(self.addrInput, 1))

	def getGameMode(self):
		try:
			mode = int(self.pm.read_float(self.addrGameMode))
		except pymem.exception.MemoryReadError as e:
			mode = -2

		return mode

	def getMenu(self):
		self.addrMenu = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU[0], ADDR_MENU[1:])
		return int.from_bytes(self.pm.read_bytes(self.addrMenu, 1))

	def getMenuCursor(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMenuCursor, 1))

	def getNormalSpeed(self):
		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		return self.pm.read_float(self.addrNormalSpeed)

	def getFocusSpeed(self):
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		return self.pm.read_float(self.addrFocusSpeed)

	def getNormalSpeedD(self):
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		return self.pm.read_float(self.addrNormalSpeedD)

	def getFocusSpeedD(self):
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])
		return self.pm.read_float(self.addrFocusSpeedD)

	def getCustomSoundId(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCustomSoundId, 1))

	def getIsBossPresent(self):
		return int.from_bytes(self.pm.read_bytes(self.addrIsBossPresent, 1))

	def getPracticeStageScore(self, characterId, shotId, difficultyId, stageId):
		return int.from_bytes(self.pm.read_bytes(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], 4))

	def getDifficultyDown(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficultyDown, 1))

	def getDifficultyUp(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficultyUp, 1))

	def getCharacterDifficulty(self, character, shot, difficulty):
		result = None
		if character == REIMU:
			if shot == SHOT_A:
				if difficulty == EASY:
					result = self.getReimuAEasy()
				elif difficulty == NORMAL:
					result = self.getReimuANormal()
				elif difficulty == HARD:
					result = self.getReimuAHard()
				elif difficulty == LUNATIC:
					result = self.getReimuALunatic()
				elif difficulty == EXTRA:
					result = self.getReimuAExtra()
				elif difficulty == PHANTASM:
					result = self.getReimuAPhantasm()
			else:
				if difficulty == EASY:
					result = self.getReimuBEasy()
				elif difficulty == NORMAL:
					result = self.getReimuBNormal()
				elif difficulty == HARD:
					result = self.getReimuBHard()
				elif difficulty == LUNATIC:
					result = self.getReimuBLunatic()
				elif difficulty == EXTRA:
					result = self.getReimuBExtra()
				elif difficulty == PHANTASM:
					result = self.getReimuBPhantasm()
		elif character == MARISA:
			if shot == SHOT_A:
				if difficulty == EASY:
					result = self.getMarisaAEasy()
				elif difficulty == NORMAL:
					result = self.getMarisaANormal()
				elif difficulty == HARD:
					result = self.getMarisaAHard()
				elif difficulty == LUNATIC:
					result = self.getMarisaALunatic()
				elif difficulty == EXTRA:
					result = self.getMarisaAExtra()
				elif difficulty == PHANTASM:
					result = self.getMarisaAPhantasm()
			else:
				if difficulty == EASY:
					result = self.getMarisaBEasy()
				elif difficulty == NORMAL:
					result = self.getMarisaBNormal()
				elif difficulty == HARD:
					result = self.getMarisaBHard()
				elif difficulty == LUNATIC:
					result = self.getMarisaBLunatic()
				elif difficulty == EXTRA:
					result = self.getMarisaBExtra()
				elif difficulty == PHANTASM:
					result = self.getMarisaBPhantasm()
		elif character == SAKUYA:
			if shot == SHOT_A:
				if difficulty == EASY:
					result = self.getSakuyaAEasy()
				elif difficulty == NORMAL:
					result = self.getSakuyaANormal()
				elif difficulty == HARD:
					result = self.getSakuyaAHard()
				elif difficulty == LUNATIC:
					result = self.getSakuyaALunatic()
				elif difficulty == EXTRA:
					result = self.getSakuyaAExtra()
				elif difficulty == PHANTASM:
					result = self.getSakuyaAPhantasm()
			else:
				if difficulty == EASY:
					result = self.getSakuyaBEasy()
				elif difficulty == NORMAL:
					result = self.getSakuyaBNormal()
				elif difficulty == HARD:
					result = self.getSakuyaBHard()
				elif difficulty == LUNATIC:
					result = self.getSakuyaBLunatic()
				elif difficulty == EXTRA:
					result = self.getSakuyaBExtra()
				elif difficulty == PHANTASM:
					result = self.getSakuyaBPhantasm()

		return result

	def getFpsText(self):
		return self.pm.read_bytes(self.addrFpsText, 8)

	def setMenuCursor(self, newCursor):
		self.pm.write_bytes(self.addrMenuCursor, bytes([newCursor]), 1)

	def setStage(self, newStage):
		self.pm.write_short(self.addrStage, newStage)

	def setDifficulty(self, newDifficulty):
		self.pm.write_short(self.addrDifficulty, newDifficulty)

	def setRank(self, newRank):
		self.pm.write_bytes(self.addrRank, bytes([newRank]), 1)

	def setCharacter(self, newCharacter):
		self.pm.write_short(self.addrCharacter, newCharacter)

	def setShotType(self, newShotType):
		self.pm.write_short(self.addrShotType, newShotType)

	def setLives(self, newLives):
		self.addrLives = getPointerAddress(self.pm, self.pm.base_address+ADDR_LIVES[0], ADDR_LIVES[1:])
		self.pm.write_float(self.addrLives, float(newLives))

	def setBombs(self, newBombs):
		self.addrBombs = getPointerAddress(self.pm, self.pm.base_address+ADDR_BOMBS[0], ADDR_BOMBS[1:])
		self.pm.write_float(self.addrBombs, float(newBombs))

	def setPower(self, newPower):
		self.addrPower = getPointerAddress(self.pm, self.pm.base_address+ADDR_POWER[0], ADDR_POWER[1:])
		self.pm.write_float(self.addrPower, float(newPower))

	def setContinues(self, newContinue):
		self.addrContinues = getPointerAddress(self.pm, self.pm.base_address+ADDR_CONTINUE[0], ADDR_CONTINUE[1:])
		self.pm.write_bytes(self.addrContinues, bytes([newContinue]), 1)

	def setNormalStartingLives(self, newNormalStartingLives):
		self.pm.write_bytes(self.addrNormalStartingLives, bytes([newNormalStartingLives]), 1)

	def setNormalContinueLives(self, newNormalContinueLives):
		self.pm.write_bytes(self.addrNormalContinueLives, bytes([newNormalContinueLives]), 1)

	def setPracticeStartingLives(self, newPracticeStartingLives):
		self.pm.write_bytes(self.addrPracticeStartingLives, bytes([newPracticeStartingLives]), 1)

	def setExtraPhantasmStartingLives(self, newExtraPhantasmStartingLives):
		self.pm.write_bytes(self.addrExtraPhantasmStartingLives, bytes([newExtraPhantasmStartingLives]), 1)

	def setStartingBombs(self, newStartingBombs):
		self.pm.write_float(self.addrStartingBombs, float(newStartingBombs))

	def setStartingPowerPoint(self, newStartingPowerPoint):
		self.pm.write_float(self.addrStartingPowerPoint, float(newStartingPowerPoint))

	def setMisses(self, newMisses):
		self.pm.write_short(self.addrMisses, newMisses)

	def setCherry(self, newCherry):
		self.addrBaseCherry = getPointerAddress(self.pm, self.pm.base_address+ADDR_BASE_CHERRY[0], ADDR_BASE_CHERRY[1:])
		base = self.pm.read_int(self.addrBaseCherry)
		self.pm.write_int(self.addrCherry, base+newCherry)

	def setCherryPlus(self, newCherryPlus):
		self.addrBaseCherry = getPointerAddress(self.pm, self.pm.base_address+ADDR_BASE_CHERRY[0], ADDR_BASE_CHERRY[1:])
		base = self.pm.read_int(self.addrBaseCherry)
		self.pm.write_int(self.addrCherryPlus, base+newCherryPlus)

	def setCherryPlusMax(self, newCherryPlusMax):
		self.pm.write_int(self.addrCherryPlusMax, newCherryPlusMax)

	def setReimuAEasy(self, newReimuAEasy):
		self.pm.write_int(self.addrReimuAEasy, newReimuAEasy)

	def setReimuANormal(self, newReimuANormal):
		self.pm.write_int(self.addrReimuANormal, newReimuANormal)

	def setReimuAHard(self, newReimuAHard):
		self.pm.write_int(self.addrReimuAHard, newReimuAHard)

	def setReimuALunatic(self, newReimuALunatic):
		self.pm.write_int(self.addrReimuALunatic, newReimuALunatic)

	def setReimuAExtra(self, newReimuAExtra):
		self.pm.write_bytes(self.addrReimuAExtra, bytes([newReimuAExtra]), 1)

	def setReimuAPhantasm(self, newReimuAPhantasm):
		self.pm.write_bytes(self.addrReimuAPhantasm, bytes([newReimuAPhantasm]), 1)

	def setReimuBEasy(self, newReimuBEasy):
		self.pm.write_int(self.addrReimuBEasy, newReimuBEasy)

	def setReimuBNormal(self, newReimuBNormal):
		self.pm.write_int(self.addrReimuBNormal, newReimuBNormal)

	def setReimuBHard(self, newReimuBHard):
		self.pm.write_int(self.addrReimuBHard, newReimuBHard)

	def setReimuBLunatic(self, newReimuBLunatic):
		self.pm.write_int(self.addrReimuBLunatic, newReimuBLunatic)

	def setReimuBExtra(self, newReimuBExtra):
		self.pm.write_bytes(self.addrReimuBExtra, bytes([newReimuBExtra]), 1)

	def setReimuBPhantasm(self, newReimuBPhantasm):
		self.pm.write_bytes(self.addrReimuBPhantasm, bytes([newReimuBPhantasm]), 1)

	def setMarisaAEasy(self, newMarisaAEasy):
		self.pm.write_int(self.addrMarisaAEasy, newMarisaAEasy)

	def setMarisaANormal(self, newMarisaANormal):
		self.pm.write_int(self.addrMarisaANormal, newMarisaANormal)

	def setMarisaAHard(self, newMarisaAHard):
		self.pm.write_int(self.addrMarisaAHard, newMarisaAHard)

	def setMarisaALunatic(self, newMarisaALunatic):
		self.pm.write_bytes(self.addrMarisaALunatic, bytes([newMarisaALunatic]), 1)

	def setMarisaAExtra(self, newMarisaAExtra):
		self.pm.write_bytes(self.addrMarisaAExtra, bytes([newMarisaAExtra]), 1)

	def setMarisaAPhantasm(self, newMarisaAPhantasm):
		self.pm.write_bytes(self.addrMarisaAPhantasm, bytes([newMarisaAPhantasm]), 1)

	def setMarisaBEasy(self, newMarisaBEasy):
		self.pm.write_int(self.addrMarisaBEasy, newMarisaBEasy)

	def setMarisaBNormal(self, newMarisaBNormal):
		self.pm.write_int(self.addrMarisaBNormal, newMarisaBNormal)

	def setMarisaBHard(self, newMarisaBHard):
		self.pm.write_int(self.addrMarisaBHard, newMarisaBHard)

	def setMarisaBLunatic(self, newMarisaBLunatic):
		self.pm.write_int(self.addrMarisaBLunatic, newMarisaBLunatic)

	def setMarisaBExtra(self, newMarisaBExtra):
		self.pm.write_bytes(self.addrMarisaBExtra, bytes([newMarisaBExtra]), 1)

	def setMarisaBPhantasm(self, newMarisaBPhantasm):
		self.pm.write_bytes(self.addrMarisaBPhantasm, bytes([newMarisaBPhantasm]), 1)

	def setSakuyaAEasy(self, newSakuyaAEasy):
		self.pm.write_int(self.addrSakuyaAEasy, newSakuyaAEasy)

	def setSakuyaANormal(self, newSakuyaANormal):
		self.pm.write_int(self.addrSakuyaANormal, newSakuyaANormal)

	def setSakuyaAHard(self, newSakuyaAHard):
		self.pm.write_int(self.addrSakuyaAHard, newSakuyaAHard)

	def setSakuyaALunatic(self, newSakuyaALunatic):
		self.pm.write_bytes(self.addrSakuyaALunatic, bytes([newSakuyaALunatic]), 1)

	def setSakuyaAExtra(self, newSakuyaAExtra):
		self.pm.write_bytes(self.addrSakuyaAExtra, bytes([newSakuyaAExtra]), 1)

	def setSakuyaAPhantasm(self, newSakuyaAPhantasm):
		self.pm.write_bytes(self.addrSakuyaAPhantasm, bytes([newSakuyaAPhantasm]), 1)

	def setSakuyaBEasy(self, newSakuyaBEasy):
		self.pm.write_int(self.addrSakuyaBEasy, newSakuyaBEasy)

	def setSakuyaBNormal(self, newSakuyaBNormal):
		self.pm.write_int(self.addrSakuyaBNormal, newSakuyaBNormal)

	def setSakuyaBHard(self, newSakuyaBHard):
		self.pm.write_int(self.addrSakuyaBHard, newSakuyaBHard)

	def setSakuyaBLunatic(self, newSakuyaBLunatic):
		self.pm.write_int(self.addrSakuyaBLunatic, newSakuyaBLunatic)

	def setSakuyaBExtra(self, newSakuyaBExtra):
		self.pm.write_bytes(self.addrSakuyaBExtra, bytes([newSakuyaBExtra]), 1)

	def setSakuyaBPhantasm(self, newSakuyaBPhantasm):
		self.pm.write_bytes(self.addrSakuyaBPhantasm, bytes([newSakuyaBPhantasm]), 1)

	def setFpsText(self, newFpsText):
		# If we have less than 8 character, we pad space character
		if len(newFpsText) < 8:
			for char in range(0, (8-len(newFpsText))):
				newFpsText.insert(0, 0x9D)
		self.pm.write_bytes(self.addrFpsText, bytes(newFpsText), 8)

	def setCharacterDifficulty(self, character, shot, difficulty, newValue):
		if character == REIMU:
			if shot == SHOT_A:
				if difficulty == EASY:
					self.setReimuAEasy(newValue)
				elif difficulty == NORMAL:
					self.setReimuANormal(newValue)
				elif difficulty == HARD:
					self.setReimuAHard(newValue)
				elif difficulty == LUNATIC:
					self.setReimuALunatic(newValue)
				elif difficulty == EXTRA:
					self.setReimuAExtra(newValue)
				elif difficulty == PHANTASM:
					self.setReimuAPhantasm(newValue)
			else:
				if difficulty == EASY:
					self.setReimuBEasy(newValue)
				elif difficulty == NORMAL:
					self.setReimuBNormal(newValue)
				elif difficulty == HARD:
					self.setReimuBHard(newValue)
				elif difficulty == LUNATIC:
					self.setReimuBLunatic(newValue)
				elif difficulty == EXTRA:
					self.setReimuBExtra(newValue)
				elif difficulty == PHANTASM:
					self.setReimuBPhantasm(newValue)
		elif character == MARISA:
			if shot == SHOT_A:
				if difficulty == EASY:
					self.setMarisaAEasy(newValue)
				elif difficulty == NORMAL:
					self.setMarisaANormal(newValue)
				elif difficulty == HARD:
					self.setMarisaAHard(newValue)
				elif difficulty == LUNATIC:
					self.setMarisaALunatic(newValue)
				elif difficulty == EXTRA:
					self.setMarisaAExtra(newValue)
				elif difficulty == PHANTASM:
					self.setMarisaAPhantasm(newValue)
			else:
				if difficulty == EASY:
					self.setMarisaBEasy(newValue)
				elif difficulty == NORMAL:
					self.setMarisaBNormal(newValue)
				elif difficulty == HARD:
					self.setMarisaBHard(newValue)
				elif difficulty == LUNATIC:
					self.setMarisaBLunatic(newValue)
				elif difficulty == EXTRA:
					self.setMarisaBExtra(newValue)
				elif difficulty == PHANTASM:
					self.setMarisaBPhantasm(newValue)
		elif character == SAKUYA:
			if shot == SHOT_A:
				if difficulty == EASY:
					self.setSakuyaAEasy(newValue)
				elif difficulty == NORMAL:
					self.setSakuyaANormal(newValue)
				elif difficulty == HARD:
					self.setSakuyaAHard(newValue)
				elif difficulty == LUNATIC:
					self.setSakuyaALunatic(newValue)
				elif difficulty == EXTRA:
					self.setSakuyaAExtra(newValue)
				elif difficulty == PHANTASM:
					self.setSakuyaAPhantasm(newValue)
			else:
				if difficulty == EASY:
					self.setSakuyaBEasy(newValue)
				elif difficulty == NORMAL:
					self.setSakuyaBNormal(newValue)
				elif difficulty == HARD:
					self.setSakuyaBHard(newValue)
				elif difficulty == LUNATIC:
					self.setSakuyaBLunatic(newValue)
				elif difficulty == EXTRA:
					self.setSakuyaBExtra(newValue)
				elif difficulty == PHANTASM:
					self.setSakuyaBPhantasm(newValue)

	def setInput(self, newInput):
		self.pm.write_bytes(self.addrInput, bytes([newInput]), 1)

	def setDifficultyDown(self, difficultyDown):
		self.pm.write_bytes(self.addrDifficultyDown, bytes([difficultyDown]), 1)

	def setDifficultyUp(self, difficultyUp):
		self.pm.write_bytes(self.addrDifficultyUp, bytes([difficultyUp]), 1)

	def setDefaultExtraDifficulty(self, cursor):
		self.pm.write_bytes(self.addrDefaultExtraDifficulty, bytes([cursor]), 1)

	def setNormalSpeed(self, newNormalSpeed):
		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		self.pm.write_float(self.addrNormalSpeed, newNormalSpeed)

	def setFocusSpeed(self, newFocusSpeed):
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		self.pm.write_float(self.addrFocusSpeed, newFocusSpeed)

	def setNormalSpeedD(self, newNormalSpeedD):
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		self.pm.write_float(self.addrNormalSpeedD, newNormalSpeedD)

	def setFocusSpeedD(self, newFocusSpeedD):
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])
		self.pm.write_float(self.addrFocusSpeedD, newFocusSpeedD)

	def resetBossPresent(self):
		self.pm.write_bytes(self.addrIsBossPresent, bytes([0]), 1)

	def setPracticeStageScore(self, characterId, shotId, difficultyId, stageId, newScore):
		return self.pm.write_int(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], newScore)

	def setKill(self, active):
		if active:
			self.pm.write_bytes(self.addrKillCondition, bytes([0x90, 0x90]), 2)
		else:
			self.pm.write_bytes(self.addrKillCondition, bytes([0x74, 0x26]), 2)

	def setLockToAllDifficulty(self):
		for lock in self.addrCharacterLock:
			self.pm.write_bytes(lock, bytes([0x7F]), 1)

	def setControllerHandler(self, activate):
		if activate:
			self.pm.write_bytes(self.addrControllerHandle, bytes([0x66, 0xA3, 0x04, 0xD9, 0x69, 0x00]), 6)
		else:
			self.pm.write_bytes(self.addrControllerHandle, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)

	def setTime(self, time):
		self.addrTime1 = getPointerAddress(self.pm, self.pm.base_address+ADDR_TIME_1[0], ADDR_TIME_1[1:])
		self.addrTime2 = getPointerAddress(self.pm, self.pm.base_address+ADDR_TIME_2[0], ADDR_TIME_2[1:])
		self.pm.write_int(self.addrTime1, time)
		self.pm.write_int(self.addrTime2, time)

	def initSoundHack(self):
		soundIdHex = hex(self.addrCustomSoundId)[2:]
		soundId = [int(soundIdHex[i:i+2], 16) for i in range(0, len(soundIdHex), 2)]
		self.pm.write_bytes(self.addrSoundHack2, bytes([0xE9, 0x1A, 0x3D, 0x22, 0x00,
														0x5D,
														0xC2, 0x08, 0x00]), 9)

		self.pm.write_bytes(self.addrSoundHack1, bytes([0x6A, 0x00,
														0xFF, 0x35, soundId[2], soundId[1], soundId[0], 0x00,
														0xB9, 0xD8, 0xA0, 0x4B, 0x00,
														0xE8, 0xAE, 0x6B, 0xE2, 0xFF,
														0xC7, 0x05, soundId[2], soundId[1], soundId[0], 0x00, 0x30, 0x00, 0x00, 0x00,
														0xE9, 0xC5, 0xC2, 0xDD, 0xFF]), 33)

	def setCustomSoundId(self, soundId = 0x0D):
		self.pm.write_bytes(self.addrCustomSoundId, bytes([soundId]), 1)

	def initStartingLives(self):
		self.pm.write_bytes(self.addrLifeHack1, bytes([0xB8, 0x00, 0x00, 0x00, 0x00, 0x90, 0x90, 0x90, 0x90, 0x90]), 10)
		self.pm.write_bytes(self.addrLifeHack2, bytes([0xB8, 0x00, 0x00, 0x00, 0x00, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 13)

	def initStartingBombs(self):
		self.pm.write_bytes(self.addrBombHack1, bytes([0xC7, 0x41, 0x68, 0x00, 0x00, 0x00, 0x00, 0xEB, 0x16]), 9)
		self.pm.write_bytes(self.addrBombHack2, bytes([0xEB, 0xE2, 0x90]), 3)

	def initPowerHack(self):
		self.pm.write_bytes(self.addrPowerHack1, bytes([0x90, 0x90]), 2)
		self.pm.write_bytes(self.addrPowerHack2, bytes([0x90, 0x90]), 2)
		self.pm.write_bytes(self.addrPowerHack3, bytes([0xD9, 0x05, 0x8B, 0xF6, 0x62, 0x00]), 6)

	def initDifficultyHack(self):
		self.pm.write_bytes(self.addrDifficutlyCondition, bytes([0xC6, 0x00]), 2)
		self.pm.write_bytes(self.addrDefaultDifficulty1, bytes([0x03]), 1)
		self.pm.write_bytes(self.addrDefaultDifficulty2, bytes([0x03]), 1)
		self.pm.write_bytes(self.addrLastDifficulty, bytes([0x03]), 1)

	def initAntiTemperHack(self):
		self.pm.write_bytes(self.addrAntiTemperHack, bytes([0x33, 0xC0, 0xC3]), 3)

	def disableDemo(self):
		self.pm.write_bytes(self.addrDemoCondtion, bytes([0xE9, 0x79, 0x01, 0x00, 0x00, 0x90]), 6)

	def setFpsUpdate(self, active):
		if active:
			self.pm.write_bytes(self.addrFpsUpdate, bytes([0x68, 0xF0, 0xE0, 0x35, 0x01]), 5)
		else:
			self.pm.write_bytes(self.addrFpsUpdate, bytes([0x68, 0x9E, 0xF6, 0x62, 0x00]), 5)

	def setFocus(self, active):
		if active:
			self.pm.write_bytes(self.addrFocusCondition, bytes([0x0F, 0x84, 0x16, 0x01, 0x00, 0x00]), 6)
		else:
			self.pm.write_bytes(self.addrFocusCondition, bytes([0xE9, 0x17, 0x01, 0x00, 0x00, 0x90]), 6)

	def setCanGetCherry(self, can):
		if can:
			self.pm.write_bytes(self.addrCherryGiveLine, bytes([0x89, 0x81, 0x1C, 0x96, 0x00, 0x00]), 6)
			self.pm.write_bytes(self.addrCherryPlusGiveLine, bytes([0x89, 0x81, 0x20, 0x96, 0x00, 0x00]), 6)
		else:
			self.pm.write_bytes(self.addrCherryGiveLine, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)
			self.pm.write_bytes(self.addrCherryPlusGiveLine, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)