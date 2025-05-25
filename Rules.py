from BaseClasses import MultiWorld
from .Variables import *
from .Regions import get_regions

def constructStageRule(player, state, nb_stage, mode, difficulty, character_list):
	rule = state.count("Lower Difficulty", player) >= difficulty
	stage_rule = False
	if mode not in NORMAL_MODE:
		if character_list:
			for character in character_list:
				stage_rule = stage_rule or (state.count(f"[{character}] Next Stage", player) >= nb_stage and state.has_any(CHARACTER_TO_ITEM[character], player))
		else:
			stage_rule = state.count("Next Stage", player) >= nb_stage
	else:
		stage_rule = True

	return rule and stage_rule

def makeStageRule(player, nb_stage, mode, difficulty, character_list):
	return lambda state: constructStageRule(player, state, nb_stage, mode, difficulty, character_list)

def makeResourcesRule(player, lives, bombs, difficulties):
	return lambda state: state.count("+1 Life", player) >= lives and state.count("+1 Bomb", player) >= bombs and state.count("Lower Difficulty", player) >= difficulties

def constructExtraRule(player, state, character_list, mode, extra):
	stage_rule = False
	if extra == EXTRA_LINEAR:
		if mode not in NORMAL_MODE:
			if character_list:
				for character in character_list:
					stage_rule = stage_rule or (state.count(f"[{character}] Next Stage", player) >= 6 and state.has_any(CHARACTER_TO_ITEM[character], player))
			else:
				stage_rule = state.count("Next Stage", player) >= 6
		else:
			stage_rule = True
	else:
		if character_list:
			for character in character_list:
				stage_rule = stage_rule or (state.has(f"[{character}] Extra Stage", player) and state.has_any(CHARACTER_TO_ITEM[character], player))
		else:
			stage_rule = state.has("Extra Stage", player)

	return stage_rule

def constructPhantasmRule(player, state, character_list, mode, phantasm, extra):
	stage_rule = False
	if phantasm == EXTRA_LINEAR:
		if mode not in NORMAL_MODE:
			number_stage = 7 if extra == EXTRA_LINEAR else 6
			if character_list:
				for character in character_list:
					stage_rule = stage_rule or (state.count(f"[{character}] Next Stage", player) >= number_stage and state.has_any(CHARACTER_TO_ITEM[character], player))
			else:
				stage_rule = state.count("Next Stage", player) >= number_stage
		else:
			stage_rule = True
	else:
		if character_list:
			for character in character_list:
				stage_rule = stage_rule or (state.has(f"[{character}] Phantasm Stage", player) and state.has_any(CHARACTER_TO_ITEM[character], player))
		else:
			stage_rule = state.has("Phantasm Stage", player)

	return stage_rule

def makeExtraRule(player, character_list, mode, extra):
	return lambda state: constructExtraRule(player, state, character_list, mode, extra)

def makePhantasmRule(player, character_list, mode, phantasm, extra):
	return lambda state: constructPhantasmRule(player, state, character_list, mode, phantasm, extra)

def makeCharacterRule(player, characters):
	return lambda state: state.has_any(characters, player)

def addDifficultyRule(player, difficulty, rule):
	return lambda state: state.count("Lower Difficulty", player) >= difficulty and rule(state)

def victoryCondition(player, state, normal, extra, phantasm, type):
	normal_victory = True
	extra_victory = True
	phantasm_victory = True

	if normal:
		endings = []
		for character in CHARACTERS_LIST:
			endings.append(f"[{character}] {ENDING_NORMAL_ITEM}")

		if type == ONE_ENDING:
			normal_victory = state.has_any(endings, player)
		elif type == ALL_CHARACTER_ENDING:
			normal_victory = state.has_all(endings, player)
		elif type == ALL_SHOT_TYPE_ENDING:
			for ending in endings:
				normal_victory = normal_victory and state.count(ending, player) >= len(SHOTS)

	if extra:
		endings = []
		for character in CHARACTERS_LIST:
			endings.append(f"[{character}] {ENDING_EXTRA_ITEM}")

		if type == ONE_ENDING:
			extra_victory = state.has_any(endings, player)
		elif type == ALL_CHARACTER_ENDING:
			extra_victory = state.has_all(endings, player)
		elif type == ALL_SHOT_TYPE_ENDING:
			for ending in endings:
				extra_victory = extra_victory and state.count(ending, player) >= len(SHOTS)

	if phantasm:
		endings = []
		for character in CHARACTERS_LIST:
			endings.append(f"[{character}] {ENDING_PHANTASM_ITEM}")

		if type == ONE_ENDING:
			phantasm_victory = state.has_any(endings, player)
		elif type == ALL_CHARACTER_ENDING:
			phantasm_victory = state.has_all(endings, player)
		elif type == ALL_SHOT_TYPE_ENDING:
			for ending in endings:
				phantasm_victory = phantasm_victory and state.count(ending, player) >= len(SHOTS)

	return normal_victory and extra_victory and phantasm_victory

def connect_regions(multiworld: MultiWorld, player: int, source: str, exits: list, rule=None):
	lifeMid = getattr(multiworld.worlds[player].options, "number_life_mid")
	bombsMid = getattr(multiworld.worlds[player].options, "number_bomb_mid")
	difficultyMid = getattr(multiworld.worlds[player].options, "difficulty_mid")
	lifeEnd = getattr(multiworld.worlds[player].options, "number_life_end")
	bombsEnd = getattr(multiworld.worlds[player].options, "number_bomb_end")
	difficultyEnd = getattr(multiworld.worlds[player].options, "difficulty_end")
	lifeExtra = getattr(multiworld.worlds[player].options, "number_life_extra")
	bombsExtra = getattr(multiworld.worlds[player].options, "number_bomb_extra")
	lifeExtra = getattr(multiworld.worlds[player].options, "number_life_phantasm")
	bombsExtra = getattr(multiworld.worlds[player].options, "number_bomb_phantasm")
	mode = getattr(multiworld.worlds[player].options, "mode")
	extra = getattr(multiworld.worlds[player].options, "extra_stage")
	phantasm = getattr(multiworld.worlds[player].options, "phantasm_stage")
	difficulty_check = getattr(multiworld.worlds[player].options, "difficulty_check")
	shot_type = getattr(multiworld.worlds[player].options, "shot_type")
	stage_unlock = getattr(multiworld.worlds[player].options, "stage_unlock")

	for exit in exits:
		rule = None
		# Rules depend on the name of the target region
		if "Mid" in exit:
			rule = makeResourcesRule(player, lifeMid, bombsMid, difficultyMid)
		elif "Late" in exit:
			rule = makeResourcesRule(player, lifeEnd, bombsEnd, difficultyEnd)
		elif "Extra" in exit and "Stage" not in exit:
			rule = makeResourcesRule(player, lifeExtra, bombsExtra, 0)
		elif "Stage" in exit:
			if "Extra" not in exit and "Phantasm" not in exit:
				level = int(exit[-1])-1
				difficulty_value = 0
				if difficulty_check in DIFFICULTY_CHECK:
					lower_difficulty = 4
					for difficulty in DIFFICULTY_LIST:
						lower_difficulty -= 1
						if difficulty in exit:
							difficulty_value = lower_difficulty
							break

				# If we don't have global stage unlock, we retrieve the character from the source region
				character_value = []
				if stage_unlock != STAGE_GLOBAL:
					if stage_unlock == STAGE_BY_CHARACTER:
						for character in CHARACTERS_LIST:
							if character in source:
								character_value = CHARACTER_SHOT_LINK[character] + [character]
								break
					else:
						if shot_type:
							for character in SHOT_TYPE_LIST:
								if character in source:
									character_value = [character]
									break
						else:
							for character in ALL_CHARACTERS_LIST:
								if character in source:
									character_value = CHARACTER_SHOT_LINK[character] + [character]
									break

				rule = makeStageRule(player, level, mode, difficulty_value, character_value)
			else:
				# If we don't have global stage unlock, we retrieve the character from the source region
				character_value = []
				if stage_unlock != STAGE_GLOBAL:
					if stage_unlock == STAGE_BY_CHARACTER:
						for character in CHARACTERS_LIST:
							if character in source:
								character_value = CHARACTER_SHOT_LINK[character] + [character]
								break
					else:
						if shot_type:
							for character in SHOT_TYPE_LIST:
								if character in source:
									character_value = [character]
									break
						else:
							for character in ALL_CHARACTERS_LIST:
								if character in source:
									character_value = CHARACTER_SHOT_LINK[character] + [character]
									break

				if "Extra" in exit:
					rule = makeExtraRule(player, character_value, mode, extra)
				else:
					rule = makePhantasmRule(player, character_value, mode, phantasm, extra)
		elif exit in ALL_CHARACTERS_LIST:
			rule = makeCharacterRule(player, CHARACTER_TO_ITEM[exit])

		sourceRegion = multiworld.get_region(source, player)
		targetRegion = multiworld.get_region(exit, player)
		sourceRegion.connect(targetRegion, rule=rule)

def set_rules(multiworld: MultiWorld, player: int):
	shot_type = getattr(multiworld.worlds[player].options, "shot_type")
	difficulty_check = getattr(multiworld.worlds[player].options, "difficulty_check")
	extra = getattr(multiworld.worlds[player].options, "extra_stage")
	phantasm = getattr(multiworld.worlds[player].options, "phantasm_stage")
	endingRequired = getattr(multiworld.worlds[player].options, "ending_required")
	goal = getattr(multiworld.worlds[player].options, "goal")

	# Regions
	regions = get_regions(shot_type, difficulty_check, extra, phantasm)

	for name, data in regions.items():
		if data["exits"]:
			connect_regions(multiworld, player, name, data["exits"])

	# Endings
	# Failsafe if the ending required is set to all shot type and the shot type are not their own checks.
	if not shot_type and endingRequired == ALL_SHOT_TYPE_ENDING:
		endingRequired = ALL_CHARACTER_ENDING

	# Check if the Extra stage is enabled if the goal is set to the Extra stage.
	if extra == NO_EXTRA and goal == ENDING_EXTRA:
		goal = ENDING_NORMAL

	# Check if the Phantasm stage is enabled if the goal is set to the Phantasm stage.
	if phantasm == NO_EXTRA and goal == ENDING_PHANTASM:
		goal = ENDING_NORMAL

	# Win condition.
	multiworld.completion_condition[player] = lambda state: victoryCondition(player, state, (goal in [ENDING_NORMAL, ENDING_ALL]), (goal in [ENDING_EXTRA, ENDING_ALL] and extra != NO_EXTRA), (goal in [ENDING_PHANTASM, ENDING_ALL] and phantasm != NO_EXTRA), endingRequired)