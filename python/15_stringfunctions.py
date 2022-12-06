Story = "once upon a time there was a boy who interested in programming"
print(len(Story))
print(Story.endswith("programming"))
#  .endswith helps to  see weather it is ended with given sentence or word
print(Story.count("a")) 
''' .count helps to count given letter or word in given command 
(cpital letters and small lettrs are different) '''
print(Story.capitalize())
''' it capitalize the first letter of a given command 
in this function it capitalize only first letter i.e o '''
print(Story.find("boy"))
''' .find function helps to find a given letter or word in commnd and tell where it lies 
 (by counting numbers) it note down only first occurance '''
print(Story.replace("boy", "legend"))
''' it replace all word (ifa same word repeated twice) like in this function i replaced
boy with legend '''