import selection
import data
import quest
import time

# クエストナンバー
q_num = 1
# パーティーメンバー
p_member = 3

# キャラクター選択、partyに格納
party = []
selection.set_party(party, data.CHARA_LIST, p_member)

# 速さ順に並び替え、p_orderに格納
p_order = quest.sort_list(party, "spd")

# 敵キャラクターをe_orderに格納
enemy = []

# クエスト開始
time.sleep(1)
quest.quest(q_num, p_order, selection.set_enemy(q_num, enemy))

print("complete!")
time.sleep(1)
q_num = 2
quest.quest(q_num, p_order, selection.set_enemy(q_num, enemy))

print("complete!\n next stage is last!")
time.sleep(1)
q_num = 3
quest.quest(q_num, p_order, selection.set_enemy(q_num, enemy))

# クエスト終了
time.sleep(1)
