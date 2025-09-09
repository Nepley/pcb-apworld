# Touhou 7 ~ Perfect Cherry Blossom Apworld

This is an implementation of touhou 7 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)<br />

## How does this randomizer work ?
At the start, you start with only one character and one shot type, with zero resources and with only the Lunatic difficulty.<br />
Each item will make it easier and easier to clear the differents stages.

## Locations
* MidBoss Defeated
* Boss Defeated
* Stage Cleared

## Items
* Characters/Shot Types
* Next Stage (Practice Mode)
* Extra Stage (If enabled)
* Phantasm Stage (If enabled)
* Continues (Normal Mode)
* Pack of 25 Power Points
* Cherry Border (If enabled)
* Lives
* Bombs
* Lower Difficulty

**Filler**: 1 Power Point

## Options
**Mode:** Practice or Normal mode.<br />
With Practice mode, you play stage by stage individually and need to unlock the stages progressively. You can also choose how the stage unlock are grouped (Globally, By character or By Shot Type)<br />
In Normal mode, you need to finish the game normally with the resources only given at the start. Futhermore, only the resources act as a gate. If you put everything at minimum in the yaml, the logic consider you can finish at sphere 1.

**Exclude Lunatic:** You can exclude the Lunatic difficulty and therefore, start with the Hard difficulty.

**Resources:** You can set the resources needed for the stages 3/4 and stages 5/6.

**Extra Stage:** You can enable the extra stage and choose if it act as the 7th stage or if it is unlocked separately. In normal mode, it is unlocked after clearing the stage 6 if it's not it's own unlock.

**Phantasm Stage:** You can enable the phantasm stage and choose if it act as the 8th stage (7th if Extra is not active or not linear) or if it is unlocked separately. In normal mode, it is unlocked after clearing the stage Extra (or stage 6 if Extra is not active or not linear) if it's not it's own unlock.

**Goal:** If the extra/phantasm stage is enabled, you can choose which goal you want between Yuyuko, Ran, Yukari or all of them.

**Endings Required:** If you must clear your goal with just one character, all of them or with all shot types if they are enabled as separate check.

**Shot Type:** If checks are separated by shot type.

**Difficulty:** If checks are separated by difficulty. In normal mode, it force the difficulty to be static. If Lunatic is excluded, no check will be behind it.

**Traps:** You can choose to have traps replacing a percentages of filler items. You can set the weight of each individual trap.

**Death Link:** You can choose to activate Death Link.

**Ring Link:** You can choose to activate Ring Link, synchronizing your gain and loss of Power Points.

## How to use

**Backup your score.dat if you care about your scores, practice stage access and Extra/Phantasm unlock**

1. Launch the game
2. Launch and connect the client "Touhou PCB" found in the archipelago launcher to the server.
3. If the message "Touhou PCB process found. Starting loop..." appeared, you're good to go
