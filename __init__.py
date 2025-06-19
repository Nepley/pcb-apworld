from typing import List
from .Variables import *

from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import TItem, get_items_by_category, item_table
from .Locations import location_table
from .Options import Th07Options
from .Regions import create_regions
from .Rules import set_rules

def launch_client():
	"""Launch a client instance"""
	from worlds.th07.Client import launch
	launch_subprocess(launch, name="GameClient")

components.append(Component(
	SHORT_NAME+" Client",
	"GameClient",
	func=launch_client,
	component_type=Type.CLIENT
))

class TWorld(World):
	game = DISPLAY_NAME
	options: Th07Options
	options_dataclass = Th07Options

	item_name_to_id = {name: data.code for name, data in item_table.items()}
	location_name_to_id = {name: id for name, id in location_table.items()}

	def fill_slot_data(self) -> dict:
		return {option_name: getattr(self.options, option_name).value for option_name in self.options_dataclass.__dataclass_fields__.keys()}

	def create_items(self):
		item_pool: List[TItem] = []
		character_list = []
		stages = []
		extra_stages = []
		phantasm_stages = []
		total_locations = len(self.multiworld.get_unfilled_locations(self.player))
		number_placed_item = 0
		mode = getattr(self.options, "mode")
		stage_unlock = getattr(self.options, "stage_unlock")
		exclude_lunatic = getattr(self.options, "exclude_lunatic")
		cherry_border = getattr(self.options, "cherry_border")
		extra = getattr(self.options, "extra_stage")
		phantasm = getattr(self.options, "phantasm_stage")
		goal = getattr(self.options, "goal")
		shot_type = getattr(self.options, "shot_type")
		difficulty_check = getattr(self.options, "difficulty_check")
		traps = getattr(self.options, "traps")
		power_point_trap = getattr(self.options, "power_point_trap")
		bomb_trap = getattr(self.options, "bomb_trap")
		life_trap = getattr(self.options, "life_trap")
		no_focus_trap = getattr(self.options, "no_focus_trap")
		reverse_movement_trap = getattr(self.options, "reverse_movement_trap")
		aya_speed_trap = getattr(self.options, "aya_speed_trap")
		freeze_trap = getattr(self.options, "freeze_trap")
		power_point_drain_trap = getattr(self.options, "power_point_drain_trap")
		no_cherry_trap = getattr(self.options, "no_cherry_trap")

		for name, data in item_table.items():
			quantity = data.max_quantity

			# Categories to be ignored, they will be added in a later stage if necessary.
			if data.category == "Filler":
				continue

			# Will be added later
			if data.category == "Traps":
				continue

			# Will be added manually later
			if data.category == "Endings":
				continue

			# Will be added later
			if data.category in ["[Global] Stages", "[Character] Stages", "[Shot Type] Stages"]:
				stages.append({"name": name, "data": data})
				continue

			# Ignored if it's not normal mode
			if data.category == "[Normal] Items" and mode == PRACTICE_MODE:
				continue

			# Will be added later
			if data.category == "Characters":
				character_list.append(name)
				continue

			# If we are in practice mode and the stage progression is not progressive, we might have to change the quantity
			if data.category == "Power Point" and mode == PRACTICE_MODE and stage_unlock != STAGE_GLOBAL:
				# If we have no addition check, we remove 3 Power Point item
				quantity = quantity-3 if not shot_type and not difficulty_check and extra == NO_EXTRA else quantity

			# Will be added later
			if data.category in ["[Global] Extra Stage", "[Character] Extra Stage", "[Shot Type] Extra Stage"]:
				extra_stages.append({"name": name, "data": data})
				continue

			# Will be added later
			if data.category in ["[Global] Phantasm Stage", "[Character] Phantasm Stage", "[Shot Type] Phantasm Stage"]:
				phantasm_stages.append({"name": name, "data": data})
				continue

			# If Lunatic is excluded, we remove one Lower difficulty
			if data.category == "Items" and name == "Lower Difficulty" and exclude_lunatic:
				quantity -= 1

			# For cherry border, we remove it if it's not randomized, or set the quantity to 1 if it's not progressive
			if data.category == "Cherry":
				if cherry_border != CHERRY_BORDER_NOT_RANDOMIZED:
					quantity = 1 if cherry_border == CHERRY_BORDER_RANDOMIZED else quantity
				else:
					continue

			item_pool += [self.create_item(name) for _ in range(0, quantity)]

		# Stages
		if mode == PRACTICE_MODE:
			# If we have stage by shot type but we don't any option adding location, we change it to stage by character
			if stage_unlock == STAGE_BY_SHOT_TYPE and not shot_type and not difficulty_check:
				stage_unlock = STAGE_BY_CHARACTER

			for stage in stages:
				quantity = stage['data'].max_quantity
				# If there is no extra stage or it's separated, we remove one stage
				if extra != EXTRA_LINEAR:
					quantity -= 1

				if phantasm != EXTRA_LINEAR:
					quantity -= 1

				if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Global] Stages":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Character] Stages":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Shot Type] Stages":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

		# Extra
		if extra == EXTRA_APART:
			# If we have stage by shot type but we don't any option adding location, we change it to stage by character
			if stage_unlock == STAGE_BY_SHOT_TYPE and not shot_type and not difficulty_check:
				stage_unlock = STAGE_BY_CHARACTER

			for stage in extra_stages:
				quantity = stage['data'].max_quantity

				if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Global] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Character] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Shot Type] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

		# Phantasm
		if phantasm == EXTRA_APART:
			# If we have stage by shot type but we don't any option adding location, we change it to stage by character
			if stage_unlock == STAGE_BY_SHOT_TYPE and not shot_type and not difficulty_check:
				stage_unlock = STAGE_BY_CHARACTER

			for stage in phantasm_stages:
				quantity = stage['data'].max_quantity

				if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Global] Phantasm Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Character] Phantasm Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Shot Type] Phantasm Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

		# Selecting starting character
		chosen = self.random.choice(character_list)
		self.multiworld.push_precollected(self.create_item(chosen))
		character_list.remove(chosen)
		for character in character_list:
			item_pool += [self.create_item(character) for _ in range(0, 1)]

		# Creating and placing Endings
		ending_normal_reimu = self.create_item("[Reimu] Ending - Yuyuko")
		ending_normal_marisa = self.create_item("[Marisa] Ending - Yuyuko")
		ending_normal_sakuya = self.create_item("[Sakuya] Ending - Yuyuko")
		ending_extra_reimu = self.create_item("[Reimu] Ending - Ran")
		ending_extra_marisa = self.create_item("[Marisa] Ending - Ran")
		ending_extra_sakuya = self.create_item("[Sakuya] Ending - Ran")
		ending_phantasm_reimu = self.create_item("[Reimu] Ending - Yukari")
		ending_phantasm_marisa = self.create_item("[Marisa] Ending - Yukari")
		ending_phantasm_sakuya = self.create_item("[Sakuya] Ending - Yukari")

		# If we have the extra stage and the extra boss is a potential goal
		if extra and goal not in [ENDING_NORMAL, ENDING_PHANTASM]:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Reimu B] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Marisa A] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				self.multiworld.get_location("[Marisa B] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				self.multiworld.get_location("[Sakuya A] Stage Extra Clear", self.player).place_locked_item(ending_extra_sakuya)
				self.multiworld.get_location("[Sakuya B] Stage Extra Clear", self.player).place_locked_item(ending_extra_sakuya)
				number_placed_item += 6
			else:
				self.multiworld.get_location("[Reimu] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Marisa] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				self.multiworld.get_location("[Sakuya] Stage Extra Clear", self.player).place_locked_item(ending_extra_sakuya)
				number_placed_item += 3

		# If we have the phantasm stage and the extra boss is a potential goal
		if phantasm and goal not in [ENDING_NORMAL, ENDING_EXTRA]:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_reimu)
				self.multiworld.get_location("[Reimu B] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_reimu)
				self.multiworld.get_location("[Marisa A] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_marisa)
				self.multiworld.get_location("[Marisa B] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_marisa)
				self.multiworld.get_location("[Sakuya A] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_sakuya)
				self.multiworld.get_location("[Sakuya B] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_sakuya)
				number_placed_item += 6
			else:
				self.multiworld.get_location("[Reimu] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_reimu)
				self.multiworld.get_location("[Marisa] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_marisa)
				self.multiworld.get_location("[Sakuya] Stage Phantasm Clear", self.player).place_locked_item(ending_phantasm_sakuya)
				number_placed_item += 3

		# If the final boss is a potential goal
		if (not extra and goal == ENDING_EXTRA) or (not phantasm and goal == ENDING_PHANTASM) or goal in [ENDING_NORMAL, ENDING_ALL]:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Reimu B] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Marisa A] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				self.multiworld.get_location("[Marisa B] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				self.multiworld.get_location("[Sakuya A] Stage 6 Clear", self.player).place_locked_item(ending_normal_sakuya)
				self.multiworld.get_location("[Sakuya B] Stage 6 Clear", self.player).place_locked_item(ending_normal_sakuya)
				number_placed_item += 6
			else:
				self.multiworld.get_location("[Reimu] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Marisa] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				self.multiworld.get_location("[Sakuya] Stage 6 Clear", self.player).place_locked_item(ending_normal_sakuya)
				number_placed_item += 3

		if traps > 0:
			remaining_locations = total_locations - (len(item_pool) + number_placed_item)

			# If we have traps, we count how many of them we need to add
			number_traps = int(remaining_locations * traps / 100)

			if number_traps > 0:
				trapList = self.random.choices(["-50% Power Point", "-1 Bomb", "-1 Life", "No Focus", "Reverse Movement", "Aya Speed", "Freeze", "Power Point Drain", "No Cherry"], weights=[power_point_trap, bomb_trap, life_trap, no_focus_trap, reverse_movement_trap, aya_speed_trap, freeze_trap, power_point_drain_trap, no_cherry_trap], k=number_traps)
				for trap in trapList:
					item_pool.append(self.create_item(trap))

		# Fill any empty locations with filler items.
		while len(item_pool) + number_placed_item < total_locations:
			item_pool.append(self.create_item(self.get_filler_item_name()))

		self.multiworld.itempool += item_pool

	def get_filler_item_name(self) -> str:
		fillers = get_items_by_category("Filler")
		weights = [data.weight for data in fillers.values()]
		return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

	def create_item(self, name: str) -> TItem:
		data = item_table[name]
		return TItem(name, data.classification, data.code, self.player)

	def set_rules(self):
		set_rules(self.multiworld, self.player)

	def create_regions(self):
		create_regions(self.multiworld, self.player, self.options)