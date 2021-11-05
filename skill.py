class Skill():
	def __init__(self, name, type):
		self.name = name
		self.type = type

class Attack(Skill):
	def __init__(self, name, type, power, whole):
		super().__init__(name, type)
		self.power = power
		self.whole = whole

class Nonattack(Skill):
	def __init__(self, name, type, value):
		super().__init__(name, type)
		self.value = value

# スキルの種類
TYPE_DICT = {
	"atk": "<攻撃>", 
	"buf": "<強化>", 
	"sup": "<支援>", 
	"dbf": "<妨害>", 
	"rec": "<回復>", 
	"hel": "<治癒>", 
}

# 攻撃
ATK_DICT = {
	"nomal": Attack("通常攻撃", TYPE_DICT["atk"], 10, False),
	"punch": Attack("パンチ", TYPE_DICT["atk"], 50, False),
	"kick": Attack("キック", TYPE_DICT["atk"], 100, False),
	"head": Attack("頭突き", TYPE_DICT["atk"], 200, False),
	"sand": Attack("砂かけ", TYPE_DICT["atk"], 30, True),
}

# 強化
BUF_DICT = {
	"con": Nonattack("集中", TYPE_DICT["buf"], 100),
}

# 支援
SUP_DICT = {
	"cheer": Nonattack("応援", TYPE_DICT["sup"], 100),
}

# 妨害
DBF_DICT = {
	"glare": Nonattack("睨む", TYPE_DICT["dbf"], 100),
}

# 回復
REC_DICT = {
	"renew": Nonattack("自己再生", TYPE_DICT["rec"], 100),
}

# 治癒
HEL_DICT = {
	"heal": Nonattack("回復魔法", TYPE_DICT["hel"], 100),
}

# スキル一覧
skills = {
	"atk": ATK_DICT,
	"buf": BUF_DICT,
	"sup": SUP_DICT,
	"dbf": DBF_DICT,
	"rec": REC_DICT,
	"hel": HEL_DICT,
}
