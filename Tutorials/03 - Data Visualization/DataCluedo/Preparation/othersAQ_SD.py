def different_idea(task,level):

	if (task=="AQ" and level=="SD1"):
		idea="An Anscombe\'s Quartet (https://en.wikipedia.org/wiki/Anscombe%27s_quartet) comprises datasets with nearly identical descriptive statistics that look different. If this idea changes measures you designed earlier or inspires you to create a new measure, try again. In case the idea information is not helpful and you are not sure if/how you might design new measures (or, revise measures you already designed), you can ask for a different idea by calling the function different_idea(\"AQ\",\"SD2\")"

	if (task=="AQ" and level=="SD2"):
		idea="Matplotlib has a handy function to generate scatterplots: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html. If this idea changes measures you designed earlier or inspires you to create a new measure, try again."

	return(idea)
