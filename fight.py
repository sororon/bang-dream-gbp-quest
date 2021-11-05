def calc_damage(ofs, dfs, hp):
	dmg = ofs*100 - dfs
	if dmg < 0:
		dmg = 0
	if dmg > hp:
		return 0
	return dmg
