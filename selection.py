import data

# 敵キャラクターのセット
def set_enemy(q_num, enemy):
	enemy = data.ENEMY_DICT[q_num]
	return enemy

# 選択されたキャラクターの表示
def show_selection(party):
	for i in range(len(party)):
		print("選択済み: ", party[i].id, party[i].name)
	return

# 能力値の表示
def show_status(c_list):
	for i in range(len(c_list)):
		pl = c_list[i]
		print(pl.id, pl.name, "HP:", pl.hp, "攻撃:", pl.atk, "防御:", pl.dfs, "技術:", pl.tec, "速さ:", pl.spd, "技１:", pl.ab1.name, pl.ab1.type, "技２:", pl.ab2.name, pl.ab2.type, "技３:", pl.ab3.name, pl.ab3.type)
	return

# キャラクターをパーティーにセットする関数
def set_party(party, c_list, count):
	print("キャラクターを" + str(count) + "人選択してください。\nもう一度選ぶと選択が解除されます")
	show_status(c_list)
	while True:
		show_selection(party)
		try:
			chara_id = input("---> ")
			chara_id = int(chara_id)
			# デバッグ用の抜け道
			if chara_id == -1:
				print("BREAK SUCCESS")
				return
			if chara_id < 1 or chara_id > len(c_list):
				#print("IndexError!")
				continue
			for i in range(chara_id):
				if int(chara_id) == i+1:
					if c_list[i].choice != True:
						c_list[i].change_choice()
						party.append(c_list[i])
					else:
						c_list[i].change_choice()
						party.remove(c_list[i])
		except ValueError:
			#print("ValueError!")
			continue
		except KeyboardInterrupt:
			#print("KeyboardInterrupt!")
			continue
		except EOFError:
			#print("EOFError!")
			continue
		if len(party) == count:
			show_selection(party)
			last_check = input("このメンバーで出撃しますか？\n0: 選び直す\nその他: 次に進む\n---> ")
			try:
				if int(last_check) == 0:
					party[count-1].change_choice()
					party.pop(count-1)
					continue
				else:
					return
			except ValueError:
				return
			except KeyboardInterrupt:
				return
