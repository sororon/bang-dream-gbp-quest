import character
import copy
import skill

# キャラクターオブジェクト
#name 	= character.Player("名前　", id,   hp, atk, dfs, tec, spd, choice, ab1, ab2, ab3)
kasumi 	= character.Player("かすみ", 1,  1600, 600, 100, 200, 600, False, skill.skills["atk"]["kick"], skill.skills["buf"]["con"], skill.skills["atk"]["punch"])
tae 	= character.Player("たえ　", 2,  2000, 800, 300, 100, 200, False, skill.skills["atk"]["head"], skill.skills["atk"]["kick"], skill.skills["rec"]["renew"])
rimi 	= character.Player("りみ　", 3,  1200, 100, 200, 600, 400, False, skill.skills["sup"]["cheer"], skill.skills["atk"]["sand"], skill.skills["atk"]["kick"])
saaya 	= character.Player("さあや", 4,  1800, 500, 500, 300, 500, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
arisa 	= character.Player("ありさ", 5,  1000, 300, 400, 800, 300, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
ran 	= character.Player("らん　", 6,  1400, 900, 100, 200, 600, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
moka 	= character.Player("もか　", 7,  1200, 300, 400, 900, 100, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
himari 	= character.Player("ひまり", 8,  1800, 400, 200, 500, 400, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
tomoe 	= character.Player("ともえ", 9,  2000, 800, 600, 100, 500, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])
tsugumi = character.Player("つぐみ", 10, 1000, 100, 300, 700, 400, False, skill.skills["atk"]["kick"], skill.skills["atk"]["kick"], skill.skills["atk"]["kick"])

#CHARA_LIST = [kasumi, tae, rimi, saaya, arisa]
CHARA_LIST = [
	copy.copy(kasumi), 
	copy.copy(tae), 
	copy.copy(rimi), 
	#copy.copy(saaya), 
	#copy.copy(arisa),
	#copy.copy(ran), 
	#copy.copy(moka), 
	#copy.copy(himari), 
	#copy.copy(tomoe), 
	#copy.copy(tsugumi),
]

# 敵キャラクターオブジェクト  ("名前　", id,  hp, atk, dfs, tec, spd)
zako 	= character.Character("ザコ　", 101, 1000, 10, 10, 10, 10)
soldier = character.Character("兵士　", 102, 5000, 100, 10, 500, 10)
boss = character.Character("ボス　", 103, 50000, 100, 100, 100, 10)

ENEMY_Q1 = [
	copy.copy(zako), 
	copy.copy(zako), 
	copy.copy(zako),
]

ENEMY_Q2 = [
	copy.copy(zako), 
	copy.copy(zako), 
	copy.copy(zako),
	copy.copy(soldier), 
	copy.copy(soldier), 
	copy.copy(soldier),
]

ENEMY_Q3 = [
	copy.copy(boss),
]

ENEMY_DICT = {
	1: ENEMY_Q1,
	2: ENEMY_Q2,
	3: ENEMY_Q3,
}
