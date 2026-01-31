from typing import Dict, NamedTuple, Optional
from .Variables import *

from BaseClasses import Item, ItemClassification

class TItem(Item):
	game: str = DISPLAY_NAME

class TItemData(NamedTuple):
	category: str
	code: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, TItemData]:
	item_dict: Dict[str, TItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, TItemData] = {
	# Items
	"+1 Life":				TItemData("Items", STARTING_ID + 0, ItemClassification.progression, 8),
	"+1 Bomb":				TItemData("Items", STARTING_ID + 1, ItemClassification.progression, 8),
	"Lower Difficulty":		TItemData("Items", STARTING_ID + 2, ItemClassification.progression, 3),
	"+1 Continue":			TItemData("[Normal] Items", STARTING_ID + 3, ItemClassification.useful, 3),
	"+25 Power Point":		TItemData("Power Point", STARTING_ID + 4, ItemClassification.useful, 5),
	"Cherry Border":		TItemData("Cherry", STARTING_ID + 5, ItemClassification.useful, 6),

	# Characters
	"Reimu A - Spirit Sign":		TItemData("Characters", STARTING_ID + 100, ItemClassification.progression),
	"Reimu B - Dream Sign":			TItemData("Characters", STARTING_ID + 101, ItemClassification.progression),
	"Marisa A - Magic Sign":		TItemData("Characters", STARTING_ID + 102, ItemClassification.progression),
	"Marisa B - Love Sign":			TItemData("Characters", STARTING_ID + 103, ItemClassification.progression),
	"Sakuya A - Illusion Sign":		TItemData("Characters", STARTING_ID + 104, ItemClassification.progression),
	"Sakuya B - Time Sign":			TItemData("Characters", STARTING_ID + 105, ItemClassification.progression),

	# Stages
	"Next Stage":					TItemData("[Global] Stages", STARTING_ID + 200, ItemClassification.progression, 7),
	"[Reimu] Next Stage":			TItemData("[Character] Stages", STARTING_ID + 201, ItemClassification.progression, 7),
	"[Marisa] Next Stage":			TItemData("[Character] Stages", STARTING_ID + 202, ItemClassification.progression, 7),
	"[Sakuya] Next Stage":			TItemData("[Character] Stages", STARTING_ID + 203, ItemClassification.progression, 7),
	"[Reimu A] Next Stage":			TItemData("[Shot Type] Stages", STARTING_ID + 204, ItemClassification.progression, 7),
	"[Reimu B] Next Stage":			TItemData("[Shot Type] Stages", STARTING_ID + 205, ItemClassification.progression, 7),
	"[Marisa A] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 206, ItemClassification.progression, 7),
	"[Marisa B] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 207, ItemClassification.progression, 7),
	"[Sakuya A] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 208, ItemClassification.progression, 7),
	"[Sakuya B] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 209, ItemClassification.progression, 7),
	"Extra Stage":					TItemData("[Global] Extra Stage", STARTING_ID + 210, ItemClassification.progression),
	"[Reimu] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 211, ItemClassification.progression),
	"[Marisa] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 212, ItemClassification.progression),
	"[Sakuya] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 213, ItemClassification.progression),
	"[Reimu A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 214, ItemClassification.progression),
	"[Reimu B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 215, ItemClassification.progression),
	"[Marisa A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 216, ItemClassification.progression),
	"[Marisa B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 217, ItemClassification.progression),
	"[Sakuya A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 218, ItemClassification.progression),
	"[Sakuya B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 219, ItemClassification.progression),
	"Phantasm Stage":				TItemData("[Global] Phantasm Stage", STARTING_ID + 220, ItemClassification.progression),
	"[Reimu] Phantasm Stage":		TItemData("[Character] Phantasm Stage", STARTING_ID + 221, ItemClassification.progression),
	"[Marisa] Phantasm Stage":		TItemData("[Character] Phantasm Stage", STARTING_ID + 222, ItemClassification.progression),
	"[Sakuya] Phantasm Stage":		TItemData("[Character] Phantasm Stage", STARTING_ID + 223, ItemClassification.progression),
	"[Reimu A] Phantasm Stage":		TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 224, ItemClassification.progression),
	"[Reimu B] Phantasm Stage":		TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 225, ItemClassification.progression),
	"[Marisa A] Phantasm Stage":	TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 226, ItemClassification.progression),
	"[Marisa B] Phantasm Stage":	TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 227, ItemClassification.progression),
	"[Sakuya A] Phantasm Stage":	TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 228, ItemClassification.progression),
	"[Sakuya B] Phantasm Stage":	TItemData("[Shot Type] Phantasm Stage", STARTING_ID + 229, ItemClassification.progression),

	# Endings
	"[Reimu] Ending - Yuyuko":		TItemData("Endings", STARTING_ID + 300, ItemClassification.progression, 2),
	"[Marisa] Ending - Yuyuko":		TItemData("Endings", STARTING_ID + 301, ItemClassification.progression, 2),
	"[Sakuya] Ending - Yuyuko":		TItemData("Endings", STARTING_ID + 302, ItemClassification.progression, 2),
	"[Reimu] Ending - Ran":			TItemData("Endings", STARTING_ID + 303, ItemClassification.progression, 2),
	"[Marisa] Ending - Ran":		TItemData("Endings", STARTING_ID + 304, ItemClassification.progression, 2),
	"[Sakuya] Ending - Ran":		TItemData("Endings", STARTING_ID + 305, ItemClassification.progression, 2),
	"[Reimu] Ending - Yukari":		TItemData("Endings", STARTING_ID + 306, ItemClassification.progression, 2),
	"[Marisa] Ending - Yukari":		TItemData("Endings", STARTING_ID + 307, ItemClassification.progression, 2),
	"[Sakuya] Ending - Yukari":		TItemData("Endings", STARTING_ID + 308, ItemClassification.progression, 2),

	# Junk
	"+1 Power Point":	TItemData("Filler", STARTING_ID + 400),

	# Trap
	"-50% Power Point":		TItemData("Traps", STARTING_ID + 500, ItemClassification.trap),
	"-1 Bomb":				TItemData("Traps", STARTING_ID + 501, ItemClassification.trap),
	"-1 Life":				TItemData("Traps", STARTING_ID + 502, ItemClassification.trap),
	"No Focus":				TItemData("Traps", STARTING_ID + 503, ItemClassification.trap),
	"Reverse Movement":		TItemData("Traps", STARTING_ID + 504, ItemClassification.trap),
	"Aya Speed":			TItemData("Traps", STARTING_ID + 505, ItemClassification.trap),
	"Freeze":				TItemData("Traps", STARTING_ID + 506, ItemClassification.trap),
	"Power Point Drain":	TItemData("Traps", STARTING_ID + 507, ItemClassification.trap),
	"No Cherry":			TItemData("Traps", STARTING_ID + 508, ItemClassification.trap),
}

item_groups: Dict[str, str] = {
	"Reimu A": ["Reimu A - Spirit Sign"],
	"Reimu B": ["Reimu B - Dream Sign"],
	"Marisa A": ["Marisa A - Magic Sign"],
	"Marisa B": ["Marisa B - Love Sign"],
	"Sakuya A": ["Sakuya A - Illusion Sign"],
	"Sakuya B": ["Sakuya B - Time Sign"]
}