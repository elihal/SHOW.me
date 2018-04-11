show_idea = [
	#structure of dictionary ["Name of show 1",0,"Top Line","Genre"]
	# First element of Show_Ideas
	["CFG",6,"Girls learn to code","Reality"],
	# Second element of Show_Ideas
	["Desperate Housewives",2,"Housewives argue","Drama"]
]

for show in show_idea:
	# show = ["CFG",6,"Girls learn to code","Reality"]
	if show[0] == "CFG":
		show[1] = show[1] + 1

print show_idea
