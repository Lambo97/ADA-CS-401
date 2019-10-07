def different_idea(task,level):

	if (task=="SC" and level=="SD1"):
		idea="Read more about correlation and causation here: https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation. If this idea changes measures you designed earlier or inspires you to create a new measure, try again. In case the idea information is not helpful and you are not sure if/how you might design new measures (or, revise measures you already designed), you can ask for a different idea by calling the function different_idea(\"SC\",\"SD2\")."

	if (task=="SC" and level=="SD2"):
		idea="Some of the correlations you found above may be spurious: https://en.wikipedia.org/wiki/Spurious_relationship -- Only include meaningful correlations to the list. If this idea changes measures you designed earlier or inspires you to create a new measure, try again. "

	return(idea)
