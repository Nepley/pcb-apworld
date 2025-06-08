from .Variables import *
from .gameController import gameController
from .Tools import *
import asyncio

class gameHandler:
	"""Class keeping track of what's unlock for the game and handling interaction with the game."""
	lives = None
	bombs = None
	power = None
	endings = None
	stages = None
	continues = None

	difficulties = None
	characters = None

	gameController = None
	lastSpeeds = []

	bossBeaten = []
	extraBeaten = []
	phantasmBeaten = []

	def __init__(self, pid):
		self.gameController = gameController(pid)
		self.reset()
		self.initGame()

	#
	# Init Resources
	#

	def giveLives(self):
		self.gameController.setLives(self.lives)

	def giveBombs(self):
		self.gameController.setBombs(self.bombs)

	def givePower(self):
		self.gameController.setPower(self.power)

	def giveContinues(self):
		self.gameController.setContinues(3 - self.continues)

	def setDifficulty(self, excludeEasy = False):
		self.gameController.setDifficulty(self.getLowestDifficulty(excludeEasy))

	def initResources(self, normalMode = False):
		if normalMode:
			self.giveContinues()

	def updateStageList(self, practiceMode = True):
		for characters in CHARACTERS:
			for shots in SHOTS:
				for difficulty in range(4):
					stage = 0
					# If we are not in practice mode, we do not update the stage
					if practiceMode and self.characters[characters][shots] and self.difficulties[difficulty]:
						stage = self.stages[characters][shots] if self.stages[characters][shots] <= 6 else 6
					self.gameController.setCharacterDifficulty(characters, shots, difficulty, stage)

	def updatePracticeScore(self, locations, checked_location):
		scores = {}
		for character in CHARACTERS:
			scores[character] = {}
			for shot in SHOTS:
				scores[character][shot] = {}
				for difficulty in range(4):
					scores[character][shot][difficulty] = {}
					for stage in range(6):
						scores[character][shot][difficulty][stage] = [0, 0, 0]

		# We check each locations to see which one has been done
		for id, location_data in locations.items():
			if id in checked_location:
				character = location_data[0]
				stage = location_data[1]
				counter = location_data[2]
				shot_type = location_data[3]
				difficulty = location_data[4]

				if difficulty >= 0:
					if shot_type in SHOTS:
						scores[character][shot_type][difficulty][stage][counter] += 1
					else:
						for shot in SHOTS:
							scores[character][shot][difficulty][stage][counter] += 1
				else:
					if shot_type in SHOTS:
						scores[character][shot_type][EASY][stage][counter] += 1
						scores[character][shot_type][NORMAL][stage][counter] += 1
						scores[character][shot_type][HARD][stage][counter] += 1
						scores[character][shot_type][LUNATIC][stage][counter] += 1
					else:
						for shot in SHOTS:
							scores[character][shot][EASY][stage][counter] += 1
							scores[character][shot][NORMAL][stage][counter] += 1
							scores[character][shot][HARD][stage][counter] += 1
							scores[character][shot][LUNATIC][stage][counter] += 1

		# We set the scores depending on the counter
		for character in CHARACTERS:
			for shot in SHOTS:
				for difficulty in range(4):
					for stage in range(6):
						score = 0
						if stage == 2:
							if scores[character][shot][difficulty][stage][0] > 0:
								score += 555550000
							if scores[character][shot][difficulty][stage][1] > 0:
								score += 5555
							if scores[character][shot][difficulty][stage][2] > 0:
								score += 222222222
							if scores[character][shot][difficulty][stage][2] > 1:
								score += 222222222
						else:
							if scores[character][shot][difficulty][stage][0] > 0:
								score += 555555555
							if scores[character][shot][difficulty][stage][1] > 0:
								score += 222222222
							if scores[character][shot][difficulty][stage][1] > 1:
								score += 222222222

						self.gameController.setPracticeStageScore(character, shot, difficulty, stage, score)

	def updateExtraUnlock(self, otherMode = False, phantasm = False):
		"""
		Update access to the Extra stage
		"""
		canExtra = self.canExtra()
		canPhantasm = self.canPhantasm()
		if canExtra or otherMode:
			for characters in CHARACTERS:
				for shots in SHOTS:
					if self.characters[characters][shots] and (self.hasExtra[characters][shots] or otherMode):
						self.gameController.setCharacterDifficulty(characters, shots, EXTRA, 99)
					else:
						self.gameController.setCharacterDifficulty(characters, shots, EXTRA, 1)
		else:
			# If we don't have Extra but we have Phantasm, we unlock the Extra like the Phantasm
			for characters in CHARACTERS:
				for shots in SHOTS:
					if self.characters[characters][shots] and (self.hasPhantasm[characters][shots]):
						self.gameController.setCharacterDifficulty(characters, shots, EXTRA, 99)
					else:
						self.gameController.setCharacterDifficulty(characters, shots, EXTRA, 1)

		if phantasm:
			for characters in CHARACTERS:
				for shots in SHOTS:
					if self.characters[characters][shots] and self.hasPhantasm[characters][shots]:
						self.gameController.setCharacterDifficulty(characters, shots, PHANTASM, 99)
					else:
						self.gameController.setCharacterDifficulty(characters, shots, PHANTASM, 0)

		# If we can only do Phantasm stage, we set the cursor default position to 1
		if canPhantasm and not canExtra:
			self.gameController.setDefaultExtraDifficulty(0x01)
		else:
			self.gameController.setDefaultExtraDifficulty(0x00)

	#
	# Boss
	#

	def isCurrentBossDefeated(self, counter):
		isDefeated = False
		# If it's the extra stage
		if self.gameController.getStage() == 7:
			isDefeated = self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter]
		# If it's the phantasm stage
		elif self.gameController.getStage() == 8:
			isDefeated = self.phantasmBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter]
		else:
			isDefeated = self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter]

		return isDefeated

	def setCurrentStageBossBeaten(self, counter, otherDifficulties = False):
		"""
		Set the boss of the current stage with the current character and shot type as beaten.
		"""

		if self.gameController.getStage() == 7:
			self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter] = True
		elif self.gameController.getStage() == 8:
			self.phantasmBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter] = True
		else:
			self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter] = True
			if otherDifficulties:
				if self.difficulties[EASY]:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][EASY][self.gameController.getStage()-1][counter] = True
				if self.difficulties[NORMAL] and self.gameController.getDifficulty() >= 1:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][NORMAL][self.gameController.getStage()-1][counter] = True
				if self.difficulties[HARD] and self.gameController.getDifficulty() >= 2:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][HARD][self.gameController.getStage()-1][counter] = True
				if self.difficulties[LUNATIC] and self.gameController.getDifficulty() >= 3:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][LUNATIC][self.gameController.getStage()-1][counter] = True

	def setBossBeaten(self, character, stage, counter, shot_type = -1, difficulty = -1):
		# If we have a valid difficulty
		if difficulty >= 0 and difficulty < 4:
			if shot_type in SHOTS:
				self.bossBeaten[character][shot_type][difficulty][stage][counter] = True
			else:
				for shot in SHOTS:
					self.bossBeaten[character][shot][difficulty][stage][counter] = True
		# If it's the Extra Stage
		elif stage == 6:
			if shot_type in SHOTS:
				self.extraBeaten[character][shot_type][counter] = True
			else:
				for shot in SHOTS:
					self.extraBeaten[character][shot][counter] = True
		# If it's the Phantasm Stage
		elif stage == 7:
			if shot_type in SHOTS:
				self.phantasmBeaten[character][shot_type][counter] = True
			else:
				for shot in SHOTS:
					self.phantasmBeaten[character][shot][counter] = True
		# Else, we check all difficulties
		else:
			if shot_type in SHOTS:
				for diff in range(4):
					self.bossBeaten[character][shot_type][diff][stage][counter] = True
			else:
				for shot in SHOTS:
					for diff in range(4):
						self.bossBeaten[character][shot][diff][stage][counter] = True

	def isBossBeaten(self, character, stage, counter, shot_type = -1, difficulty = -1):
		flags = []
		# If we have a valid difficulty
		if difficulty >= 0 and difficulty < 4:
			if shot_type in SHOTS:
				flags.append(self.bossBeaten[character][shot_type][difficulty][stage][counter])
			else:
				for shot in SHOTS:
					flags.append(self.bossBeaten[character][shot][difficulty][stage][counter])
		# If it's the Extra Stage
		elif stage == 6:
			if shot_type in SHOTS:
				flags.append(self.extraBeaten[character][shot_type][counter])
			else:
				for shot in SHOTS:
					flags.append(self.extraBeaten[character][shot][counter])
		# If it's the Phantasm Stage
		elif stage == 7:
			if shot_type in SHOTS:
				flags.append(self.phantasmBeaten[character][shot_type][counter])
			else:
				for shot in SHOTS:
					flags.append(self.phantasmBeaten[character][shot][counter])
		# Else, we check all difficulties
		else:
			if shot_type in SHOTS:
				for diff in range(4):
					flags.append(self.bossBeaten[character][shot_type][diff][stage][counter])
			else:
				for shot in SHOTS:
					for diff in range(4):
						flags.append(self.bossBeaten[character][shot][diff][stage][counter])

		return True if True in flags else False

	#
	# Get Handler Functions
	#

	def getLives(self):
		return self.lives

	def getBombs(self):
		return self.bombs

	def getPower(self):
		return self.power

	def getEndings(self):
		return self.endings

	def getLowestDifficulty(self, excludeEasy = False):
		"""
		Retrieve the lowest difficulty unlocked.
		"""
		difficulty = 3
		if(self.difficulties[EASY] and not excludeEasy):
			difficulty = 0
		elif(self.difficulties[NORMAL] or (self.difficulties[EASY] and excludeEasy)):
			difficulty = 1
		elif(self.difficulties[HARD]):
			difficulty = 2

		return difficulty

	def canExtra(self):
		"""
		If any character can access to the Extra stage.
		"""
		can = False
		for character in CHARACTERS:
			for shot in SHOTS:
				if self.characters[character][shot] and self.hasExtra[character][shot]:
					can = True
					break
			if can:
				break

		return can

	def canPhantasm(self):
		"""
		If any character can access to the Phantasm stage.
		"""
		can = False
		for character in CHARACTERS:
			for shot in SHOTS:
				if self.characters[character][shot] and self.hasPhantasm[character][shot]:
					can = True
					break
			if can:
				break

		return can

	#
	# Get Games Functions
	#

	def getGameMode(self):
		return self.gameController.getGameMode()

	def getMenu(self):
		return self.gameController.getMenu()

	def getDifficulty(self):
		return self.gameController.getDifficulty()

	def getMisses(self):
		return self.gameController.getMisses()

	def getCurrentLives(self):
		return self.gameController.getLives()

	def isBossPresent(self):
		return self.gameController.getIsBossPresent() == 1

	def getCurrentStage(self):
		return self.gameController.getStage()

	def getCurrentPowerPoint(self):
		return self.gameController.getPower()

	def getCurrentScore(self):
		return self.gameController.getScore()

	def getCurrentContinues(self):
		return self.gameController.getContinues()

	#
	# Set Items Functions
	#

	def addLife(self, addInLevel = True):
		if(self.lives < 8):
			self.lives += 1

		self.gameController.setPracticeStartingLives(self.lives)
		self.gameController.setNormalStartingLives(self.lives)
		self.gameController.setNormalContinueLives(self.lives)
		self.gameController.setExtraPhantasmStartingLives(self.lives)

		if addInLevel and self.gameController.getGameMode() == IN_GAME:
			self.gameController.setLives(self.gameController.getLives() + 1)

	def addBomb(self, addInLevel = True):
		if(self.bombs < 8):
			self.bombs += 1

		self.gameController.setStartingBombs(self.bombs)

		if addInLevel and self.gameController.getGameMode() == IN_GAME:
			self.gameController.setBombs(self.gameController.getBombs() + 1)

	def add1Power(self, addInLevel = True):
		if(self.power < 128):
			self.power += 1

		self.gameController.setStartingPowerPoint(self.power)

		if addInLevel and self.gameController.getGameMode() == IN_GAME and self.gameController.getPower() < 128:
			self.gameController.setPower(self.gameController.getPower() + 1)

	def add25Power(self, addInLevel = True):
		if(self.power < 103):
			self.power += 25
		else:
			self.power = 128

		self.gameController.setStartingPowerPoint(self.power)

		if addInLevel and self.gameController.getGameMode() == IN_GAME:
			if self.gameController.getPower() < 103:
				self.gameController.setPower(self.gameController.getPower() + 25)
			else:
				self.gameController.setPower(128)

	def addStage(self, extra = False, phantasm = False, character = -1, shot_type = -1):
		character_list = [character] if character > -1 else CHARACTERS
		shot_type_list = [shot_type] if shot_type > -1 else SHOTS

		for character in character_list:
			for shot in shot_type_list:
				self.stages[character][shot] += 1

				if(self.stages[character][shot] > 6 and extra):
					self.unlockExtraStage(character, shot)

				if (self.stages[character][shot] > 6 and not extra and phantasm) or (self.stages[character][shot] > 7 and extra and phantasm):
					self.unlockPhantasmStage(character, shot)

	def addContinue(self):
		if(self.continues < 3):
			self.continues += 1

	def addEnding(self, character, type):
		self.endings[character][type] += 1

	def unlockDifficulty(self, difficulty):
		self.difficulties[difficulty] = True

	def unlockExtraStage(self, character = -1, shot_type = -1):
		# Unlock for one character/shot type
		if character > -1 and shot_type > -1:
			self.hasExtra[character][shot_type] = True
		# Unlock for one character
		elif character > -1:
			for shot in SHOTS:
				self.hasExtra[character][shot] = True
		# Unlock for all characters
		else:
			for character in CHARACTERS:
				for shot in SHOTS:
					self.hasExtra[character][shot] = True

	def unlockPhantasmStage(self, character = -1, shot_type = -1):
		# Unlock for one character/shot type
		if character > -1 and shot_type > -1:
			self.hasPhantasm[character][shot_type] = True
		# Unlock for one character
		elif character > -1:
			for shot in SHOTS:
				self.hasPhantasm[character][shot] = True
		# Unlock for all characters
		else:
			for character in CHARACTERS:
				for shot in SHOTS:
					self.hasPhantasm[character][shot] = True

	def unlockCharacter(self, character, shot):
		self.characters[character][shot] = True

	#
	# Traps
	#

	def halfPowerPoint(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() // 2)

	def loseBomb(self):
		if(self.gameController.getBombs() > 0):
			self.gameController.setBombs(self.gameController.getBombs() - 1)

	def loseLife(self):
		if(self.gameController.getLives() > 0):
			self.gameController.setLives(self.gameController.getLives() - 1)

	def powerPointDrain(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() - 1)

	def canFocus(self, can):
		self.gameController.setFocus(can)

	def reverseControls(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()*-1)
		self.gameController.setFocusSpeed(self.gameController.getFocusSpeed()*-1)
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()*-1)
		self.gameController.setFocusSpeedD(self.gameController.getFocusSpeedD()*-1)

	def ayaSpeed(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()*4)
		self.gameController.setFocusSpeed(self.gameController.getFocusSpeed()/4)
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()*4)
		self.gameController.setFocusSpeedD(self.gameController.getFocusSpeedD()/4)

	def freeze(self):
		self.lastSpeeds = [self.gameController.getNormalSpeed(), self.gameController.getFocusSpeed(), self.gameController.getNormalSpeedD(), self.gameController.getFocusSpeedD()]
		self.gameController.setNormalSpeed(0.0)
		self.gameController.setFocusSpeed(0.0)
		self.gameController.setNormalSpeedD(0.0)
		self.gameController.setFocusSpeedD(0.0)

	def resetSpeed(self):
		self.gameController.setNormalSpeed(self.lastSpeeds[0])
		self.gameController.setFocusSpeed(self.lastSpeeds[1])
		self.gameController.setNormalSpeedD(self.lastSpeeds[2])
		self.gameController.setFocusSpeedD(self.lastSpeeds[3])

	#
	# Other
	#

	def reconnect(self, pid):
		self.gameController = gameController(pid)
		self.initGame()

	def initGame(self):
		self.gameController.initStartingLives()
		self.gameController.initStartingBombs()
		self.gameController.initPowerHack()

		self.gameController.setPracticeStartingLives(self.lives)
		self.gameController.setExtraPhantasmStartingLives(self.lives)
		self.gameController.setNormalStartingLives(self.lives)
		self.gameController.setNormalContinueLives(self.lives)
		self.gameController.setStartingBombs(self.bombs)
		self.gameController.setStartingPowerPoint(self.power)

		self.gameController.initSoundHack()
		self.gameController.initDifficultyHack()
		self.gameController.setLockToAllDifficulty()
		self.gameController.disableDemo()

	def reset(self):
		"""
		Method that initialize all the variables to their default values.
		"""
		# Default Value
		self.lives = 0
		self.bombs = 0
		self.power = 0
		self.continues = 0

		self.stages = {}
		for character in CHARACTERS:
			self.stages[character] = {}
			for shot in SHOTS:
				self.stages[character][shot] = 1

		self.endings = {}
		for character in CHARACTERS:
			self.endings[character] = {}
			for ending in ENDINGS:
				self.endings[character][ending] = 0

		self.hasExtra = {}
		for character in CHARACTERS:
			self.hasExtra[character] = {}
			for shot in SHOTS:
				self.hasExtra[character][shot] = False

		self.hasPhantasm = {}
		for character in CHARACTERS:
			self.hasPhantasm[character] = {}
			for shot in SHOTS:
				self.hasPhantasm[character][shot] = False

		self.difficulties = {LUNATIC: True, HARD: False, NORMAL: False, EASY: False}

		self.characters = {}
		for character in CHARACTERS:
			self.characters[character] = {}
			for shot in SHOTS:
				self.characters[character][shot] = False

		self.bossBeaten = {}
		for character in CHARACTERS:
			self.bossBeaten[character] = {}
			for shot in SHOTS:
				self.bossBeaten[character][shot] = {}
				for difficulty in range(4):
					self.bossBeaten[character][shot][difficulty] = [[False, False], [False, False], [False, False, False], [False, False], [False, False], [False, False]]

		self.extraBeaten = {}
		for character in CHARACTERS:
			self.extraBeaten[character] = {}
			for shot in SHOTS:
				self.extraBeaten[character][shot] = [False, False]

		self.phantasmBeaten = {}
		for character in CHARACTERS:
			self.phantasmBeaten[character] = {}
			for shot in SHOTS:
				self.phantasmBeaten[character][shot] = [False, False]

		self.lastSpeeds = [0, 0, 0, 0]

	def playSound(self, soundId):
		self.gameController.setCustomSoundId(soundId)

	async def killPlayer(self):
		self.gameController.setKill(True)
		await asyncio.sleep(0.1)
		self.gameController.setKill(False)

	def giveCurrentPowerPoint(self, power):
		"""
		Give power point to the current stage
		"""
		if self.gameController.getGameMode() == IN_GAME:
			new_power = self.gameController.getPower() + power
			if(new_power > 128):
				new_power = 128
			elif(new_power < 0):
				new_power = 0

			self.gameController.setPower(new_power)

	def resetStageVariables(self):
		"""
		Method to be called when leaving a stage and reset the stage variables.
		"""
		self.gameController.resetBossPresent()

	def updateCursor(self, minValue = -1):
		"""
		Update the minimum cursor position value authorized.
		If -1, it will be the lowest difficulty.
		If -2, it will lock to 1 if the Extra Stage is not unlocked by any character. (For Phantasm select)
		"""
		if minValue == -2:
			minValue = 1 if not self.canExtra() else 0
		else:
			minValue = self.getLowestDifficulty() if minValue == -1 else minValue
		self.gameController.setDifficultyDown(minValue)
		self.gameController.setDifficultyUp(minValue)

		# If the cursor is "out of bounds", we set it to the minimum value authorized
		if self.gameController.getMenuCursor() < minValue:
			self.gameController.setMenuCursor(minValue)

	async def displayMessage(self, text, color, timer = 2):
		"""
		Display text in game
		"""
		try:
			self.gameController.setFpsUpdate(False)

			if color in [WHITE_TEXT, BLUE_TEXT]:
				text_color = False if WHITE_TEXT else True
				textToDisplay = textToBytes(text, text_color)
				self.gameController.setFpsText(textToDisplay)
				await asyncio.sleep(timer)
			elif color == FLASHING_TEXT:
				currentTimer = timer
				text_color = True
				while currentTimer > 0:
					textToDisplay = textToBytes(text, text_color)
					self.gameController.setFpsText(textToDisplay)
					currentTimer -= 0.5
					text_color = not text_color
					await asyncio.sleep(0.5)

			self.gameController.setFpsUpdate(True)
		except Exception as e:
			pass

	def checkIfCurrentIsPossible(self, isNormalMode = False):
		"""
		Check if the current combinaison is a possible one we what is unlocked
		"""
		possible = True

		# Check difficulty
		if self.getDifficulty() < self.getLowestDifficulty():
			possible = False

		# Check character
		if not self.characters[self.gameController.getCharacter()][self.gameController.getShotType()]:
			possible = False

		# Check stage
		if not isNormalMode and (self.gameController.getStage() > self.stages[self.gameController.getCharacter()][self.gameController.getShotType()] and self.gameController.getStage() != 7) and (self.gameController.getStage() == 7 and self.hasExtra[self.gameController.getCharacter()][self.gameController.getShotType()]):
			possible = False

		return possible