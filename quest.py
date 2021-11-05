from operator import attrgetter
import fight
import skill

# リストをkeyの降順で返す関数
def sort_list(lst, key):
	new_lst = sorted(lst, key=attrgetter(key), reverse=True)
	return new_lst

# main.py -> quest.py
def quest(q_num, p_order, e_order):
	show_situation(q_num, p_order, e_order)
	if p_order == []:
		return
	# 敵味方を速さ順に並び替え、all_orderに格納
	all_order = p_order + e_order
	all_order = sort_list(all_order, "spd")
	# 速さ順に行動
	turn = 1
	while True:
		print("turn: ", turn)
		show_situation(q_num, p_order, e_order)
		for i in range(len(all_order)):
			action = select_action(all_order[i])
			print("action: ", action)
			if action == -1:
				print("BREAK SUCCESS.")
				return
			# 敵
			if action == 0:
				continue
			action_junction(all_order[i], action, e_order)
			show_process(p_order, e_order)
			cnt = 0
			for j in range(len(e_order)):
				cnt += e_order[j].hp
			if cnt <= 0:
				print("全ての敵を倒した！")
				return

# キャラクターの名前と体力表示
def show_process(p_order, e_order):
	print("《現在の戦況》\n〔味方陣営〕")
	for i in range(len(p_order)):
		print(p_order[i].name, "HP:", p_order[i].hp)
	print("\n〔敵陣営〕")
	for i in range(len(e_order)):
		print(e_order[i].name, "HP:", e_order[i].hp)
	return

# 現在の戦況の表示
def show_situation(q_num, p_order, e_order):
	print("\n~~~ Quest", q_num, " ~~~\n")
	show_process(p_order, e_order)
	return

# キャラクターの行動選択
def select_action(player):
	# 敵の場合
	if player.id > 100 and int(player.hp) > 0:
		print("enemy turn")
		return 0
	if int(player.hp) > 0:
		show_action(player)
		while True:
			try:
				action = input("---> ")
				action = int(action)
				if action == -1:
					print("BREAK SUCCESS.")
					return action
				if action < -1 or action > 3:
					#print("IndexError!")
					continue
				# 正しい入力
				return action
			except ValueError:
				continue
			except KeyboardInterrupt:
				continue
			except EOFError:
				continue

# 行動手段の表示
def show_action(player):
	print("\n" + player.name + "の行動を選んでください。\n0.通常攻撃\n1.", player.ab1.name, player.ab1.type, "\n2.", player.ab2.name, player.ab2.type, "\n3.", player.ab3.name, player.ab3.type)
	return

# 攻撃手段により内部処理の分岐
def action_junction(player, action, e_order):
	if action == 0:
		decide_action(player, skill.skills["atk"]["nomal"], e_order)	
	elif action == 1:
		decide_action(player, player.ab1, e_order)
	elif action == 2:
		decide_action(player, player.ab2, e_order)	
	elif action == 3:
		decide_action(player, player.ab3, e_order)	
	return

def decide_action(player, ability, e_order):
	# 敵への攻撃
	if ability.type == skill.TYPE_DICT["atk"]:
		print("attack")
		# 全体攻撃
		if ability.whole:
			print("全体攻撃開始！")
			for i in range(len(e_order)):
				if e_order[i].hp > 0:
					e_order[i].hp = fight.calc_damage(player.atk, e_order[i].dfs, e_order[i].hp)
					show_attack(player, e_order[i])
					check_hp(e_order[i].hp)
			return
		# 単体攻撃
		target = select_direction(e_order)
		if target == -1:
			return
		enemy = e_order[target-1]
		enemy.hp = fight.calc_damage(player.atk, enemy.dfs, enemy.hp)
		show_attack(player, enemy)
		check_hp(enemy.hp)
		return
	# 自己強化
	elif ability == skill.TYPE_DICT["buf"]:
		pass
	# 味方バフ
	elif ability == skill.TYPE_DICT["sup"]:
		pass
	# 敵デバフ
	elif ability == skill.TYPE_DICT["dbf"]:
		pass
	# 自己回復
	elif ability == skill.TYPE_DICT["rec"]:
		pass
	# 味方回復
	elif ability == skill.TYPE_DICT["hel"]:
		pass
	else:
		print("error")
	return

def show_attack(player, enemy):
	print(player.name, "の攻撃！")
	print(enemy.name, "にダメージ！")
	return

# 攻撃対象の決定
def select_direction(e_order):
	print("\nどの敵に攻撃？")
	for i in range(len(e_order)):
		if e_order[i].hp > 0:
			print(i+1, e_order[i].name)
	while True:
		try:
			target = input("--->")
			target = int(target)
			# デバッグ用の抜け道
			if target == -1:
				print("BREAK SUCCESS")
				return target
			if target < 1 or target > len(e_order):
				#print("IndexError!")
				continue
			if e_order[target-1].hp <= 0:
				continue
			break
		except ValueError:
			continue
		except KeyboardInterrupt:
			continue
		except EOFError:
			continue
	return target

def check_hp(hp):
	if hp < 0:
		print("もう戦える体力がない！")
	return
