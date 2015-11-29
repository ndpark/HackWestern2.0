
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def main():
	print """
	 _   _            _      _    _           _                    ____   _____ 
	| | | |          | |    | |  | |         | |                  / __  \|  _  |
	| |_| | __ _  ___| | __ | |  | | ___  ___| |_ ___ _ __ _ __   `' / /'| |/' |
	|  _  |/ _` |/ __| |/ / | |/\| |/ _ \/ __| __/ _ \ '__| '_ \    / /  |  /| |
	| | | | (_| | (__|   <  \  /\  /  __/\__ \ ||  __/ |  | | | | ./ /___\ |_/ /
	\_| |_/\__,_|\___|_|\_\  \/  \/ \___||___/\__\___|_|  |_| |_| \_____(_)___/ 
																	- by Andy Park, hg4park@uwaterloo.ca
	"""
	print "Welcome to HackWestern!"
			
def beginning():
	
	print """\n
	-If you would like to go to registration, please enter 1!
	-If not, please enter 2
	-If you would like to quit (COWARD!!), please type "I'm a loser"
	"""
	Choice = raw_input('>')
			
	for case in switch(Choice):
		if case('1'):
			print ">>You made it! What is your name?"
			name = raw_input('Name: ')
			print "\n>>Hello %s, where are you from?" %name
			location = raw_input ('Location: ')
			print "\n>>Wow, you're from %s ?? No way!" %location
			print ">>Last thing, what are you planning to make?"
			project = raw_input('\nProject? ')
			print "\n>>Dope %s, that's a sick project. Making %s !!" %(name,project)
			print "\t>>You're now registered! Have fun!!\n"
			break
			
		if case('2'):
			print "\n>>Are you sure? Are you not registered?"
			print ">>If you are not registered, you can still register! (aka. play the game)"
			print ">>Type 'y/Y' if you want to go in, type 'n/N' if you did not mean to come here at all"
			leave = raw_input('\'y\' to go in, \'n\'to leave: ')
			if leave == "Y":
				print "\n\n>>Yay! Let's try this again"
			beginning()
			break
			
			if leave == "N":
				print "\n>>Aww bye!"
			exit()
			
		if case("I'm a loser"):
			print "\n>>See ya later aligator"
			exit()
			
		if case():
			print "\n>>INPUT ERROR! 101010100101010001010101011101010 (I actually don't know binary)"
			print ">>Please try again!"
			beginning()
			break
def afterRegistration():
	print """\nWhere would you like to go?
	Enter 1 for Gym 
	Enter 2 for Cafeteria
	Enter 3 for Bathroom
	Enter 4 for Mysterious Dungeon
	Enter 5 to get out of here because \'I DON\'T BELONG HERE!!!!!!!!!!\'
	Enter 6 to explore
	You only get to go to three of these, pick wisely!"""

	where = raw_input('Where? ')
	for case in switch(where):
		if case('1'):
			print "\n>>This is where all the sponsors are!"
			print ">>Would you like to talk to them?"
			ans = raw_input('\'Y\' to talk, or \'N\' to skidaddle out of here: ')
			if ans.upper() == 'Y':
				print """\nYou talked to alot of cool sponsors such as:
				
			InfoTech, MLH, Digital Boundary Group, Propel, Big Viking Games, techalliance, 
			CityWide, Magnet, LEDC, OCE, ONE, Shopify, pwc, rhinoactive, MtnDew, bigbluebubble,
			Communitech, RaceRoster, SharcNet, Particle, Strategyzer, WolframAlpha, goviral
			YOU GOT SO MUCH SWAG!! SO HAPPY!!!
				Let's go somewhere else now\n"""
			else:
				print ">>Let's skidaddle out of here dawg\n"
			break
		if case('2'):
			print ">>Food! You got a delicious meal of pasta, salad, and bread\n"
			break
		if case('3'):
			bathroom()
			break
					
		if case('4'):
			print ">>Welcome to Mystery dungeon"
			print ">>You see a ghost of Steve Jobs"
			print ">>He offfers you a job"
			print ">>YOU'RE HIRED AT APPLE!!!!!!!!!!!!!!!!"
			print ">>You leave HackWestern because who cares anymore"
			print ">>\nIf you want to offer me a job please contact Andy Park at hg4park@uwaterloo.ca"
			leave = raw_input('Would you like to leave? You have got a job anyways (Y/N)')
			if leave.upper() == 'Y':
				print "\n>>Bye bye! I'll miss you\n"
				exit()
				break
			if leave.upper() == 'N':
				print "\n>>Glad you decided to stay\n"
				break
			else:
				print "\n>>I guess you're staying!"
			break
			exit()
		
		if case('5'):
			print ">>I\'m not stuck in here with you, you\'re stuck in here with me!"
			print ">>Jk! if you want to get out, you're free to go!"
			leave = raw_input('Would you like to leave?')
			if leave.upper() == 'Y':
				print ">>Bye bye! I'll miss you\n"
				exit()
				break
			if leave.upper() == 'N':
				print ">>Glad you decided to stay\n"
				break
			break
			
		if case('6'):
			print ">>Western is pretty nice!! But WATER WATER WATER, LOO LOO LOO!!"
			break
		if True: 
			print ">>Not a valid choice dawg. Let's try this again"
			afterRegistration()
			break

def afterAfterRegistration():
	
	print """
	After chilling for a bit and doing the three things you chose above, 
	
	ORIENTATION TAKES PLACE!!!!............
	
	"""

	print "\n>>The orientation was dope. The organizers are super chill. Sponsors are super duper amazing. You feel motivated"
	print ">>You meet up with your team that you met through facebook, they're super cool - Shelly, Henri, and Carolina"
	print ">>You all brainstorm through ideas and finally narrow it down to 5 ideas "

def bathroom():
	print """ What would you like to do in here?
	1 - Poopoo
	2 - Peepee
	3 - Admire others
	4 - Wash hands then get out"""
	washroom = raw_input('Pick one! ')
	for case in switch(washroom):
		if case('1'):
			print ">>You take the biggest dump ever"
			break
		if case('2'):
			print ">>Whew! that busride here made my bladder really full!"
			break
		if case('3'):
			print ">>People seem uneasy. You reassure them by saying you're only looking at their pebble."
			print ">>If you are a girl then I have no idea what would make girls feel uneasy"
			break
		if case('4'):
			print ">>Gotta clean them hands!"
		else:
			print ">>Please pick a valid choice"
			bathroom()
			break

def projects():
	print """
	Which project would you like to tackle?:
	1 - Make a webapp game using Bitalino called ArmStrong!
		Sends an arm rocket to the moon. It uses the EMG to measures
		if you are flexing, and flexing powers the arm rocket to the moon.
		
	2 - A Tinder-like Android app for hackers called Hackr!
		It matches you with hackers nearby, who could become your lovers.
		For those socially inept hackers, it suggests great pickup lines!
		"Where front-end meets back-end."
	
	3 - Come up with a text-based game about your experience at HackWestern
		(HIGHLY RECOMMENDED IT'S GONNA BE THE BEST IDEA EVER)
		
	4 - Making a troll website which makes your curser invisible!
		But wait! There's more! It'll have different cursers on screen moving around
		Your goal is to press the button in the middle.
		
	5 - The original project you had in mind!
		
	
	""" 
	choice = raw_input('Project choice: ')
	for case in switch(choice):
		if case('1'):
			print ">>You try for 8 hours to process data from Bitalino through python"
			print ">>You fail miserably, and give up"
			projects()
			break
		if case('2'):
			print ">>You realize no one on your team has java/ android development experience"
			print ">>Darn."
			projects()
			break
		if case('3'):
			print ">>You decide ambitiously to make a text-based game with your limited knowledge of python"
			print ">>Sounds cool! Let's try it!!"
			break
		if case('4'):
			print ">>Caroline is a web God and she develops the website within hours"
			print ">>Hm.. now what should we do?"
			projects()
			break
		if case('5'):
			print ">>You decide that this project idea is decent at best. Meh."
			projects()
			break
		if case(): # default, could also just omit condition or 'if True'
			print ">>DAWG WHAT ARE YOU DOING PICK SOMETHING"
			break

def working():
	print """
	After hours of work, you decide to make the coolest text-based game ever.
	BUT you forgot almost everything about Python.
	Thankfully, you wrote down notes while teaching yourself python.
	HOWEVER you realize that Python does not have a 'switch' function
	What will you do?
	
	Type:
	'NotRickAstley' - Give up.
	'Google' - Google how to!
	'Bing' - Bing how to!
	(CasE insensiTive)
	"""
	search = raw_input('What will it be?: ')
	search = search.upper()
	for case in switch(search):
		if case('GOOGLE'):
			print "\n>>You found a way! You can now make a cool game"
			break
		if case('BING'):
			print ">>\nStop lying to yourself."
			print ">>You google the problem and find the right answer."
			break
		if case('NOTRICKASTLEY'):
			print ">>\nYOU GAVE UP! YOU ARE A DISGRACE!"
			print ">>You decide to sleep instead."
			print "............................................"
			print ">>You sleep through the whole weekend, what a waste of time"
			print "\n\n Well, the Hackathon's over!"
			print "\n\t\t THANK YOU FOR PLAYING! Please try different combinations next time!!!!"
			quit()
			break
		if case(): # default, could also just omit condition or 'if True'
			print "\n>>Try again!"
			working()
			break
		
def working2():
	print "\nWhile working, a person from Communitech drops in and asks about what you're working on"
	answer = raw_input('>>Should you be honest about it lie to look cool? (Truth/Lie)? ')
	answer = answer.upper()
	if answer == 'TRUTH':
		print "\n>>I am working on a dope text-based game about this very Hackathon!"
		print ">>Communitech guy: \"Sick man, keep working on it\""
		print ">>You get a huge confidence boost and get alot of stuff done within the next 5 hours"
	
	elif answer =='LIE':
		print "\n>>Communitech guy looks at your screen and realizes that you are lying"
		print ">>Communitech guy: \"YOU LIED! YOU HAVE BEEN SHUNNED. In order to revoke this status, you must beat me in a code battle.\""
		print ">>Do you accept this challenge?"
		fight = raw_input('(Y/N)? ')
		fight = fight.upper()
		if fight == 'Y':
			print "\n>>After an intense battle,"
			print ">>Your coding skills somehow prove to be superior than the Communitech guy"
			print ">>Communitech guy offers you a job, which you gladly accept."
			print ">>Job title: Ninja coder."
		elif fight == 'N':
			print "\n>>Communitech guy calls you a coward and laughs at you"
			print ">>Everybody joins"
			print ">>You start crying and spaghetti falls out of your pants."
			print ">>You give up on coding, and join a monastery in China to become a monk"
			print "\n\t\t THANK YOU FOR PLAYING! Please try different combinations next time!!!!"
			quit()
				
def sleep():
	print """
		\n>>Now, now, it has been a long day of coding, and you are quite weary

	THE ULTIMATE QUESTION: SHOULD YOU SLEEP?
		"""
	answer = raw_input('(Y/N)? ')
	answer = answer.upper()
	
	if answer == 'Y':
		print "\n>>You get a blessed night's sleep and wake up rejuvenated, ready for the next day"
		
	if answer == 'N':
		print "\n>>You stay awake ALL NIGHT"
		print ">>Get everything done"
		print ">>Now you can play around and go visit your frineds!"
		print ">>But you're super tired tho so"
		print ">>YOU FALL ASLSEEP AND ACCIDENTALLY MISS EVERYTHING, including to sumbit this game. OH NO"
		print ">>\n\n\tTHANK YOU FOR PLAYING! Please try different combinations next time!!!!"
		print "(for example, select Y for this question.)"
		quit()
		
def day2():
	print "\n>>It is 11 am and you get straight back to coding. I forgot to mention that you had food last night."
	print ">>You get lunch. Burritos from Burrito Boys. Delicious."
	print "\n\n>>After lunch, a person from Big Viking Games comes to check out your DOPE game he heard about from a Communitech guy."
	print ">>They challenge you to a code battle . Do you accept?\n"
	answer = raw_input('(Y/N)? ')
	answer = answer.upper()
	
	if answer == 'Y':
		print """ 
		The battle is in Python, which you have been practicing for the past 24 hours. This is an easy battle.
		As you code away, the expression on the Big Viking Games guy changes from confident to absolute horror.
		The time is up. You are the winner. It was an easy win for you.
		You are now deemed as the King of the Vikings. It is a good day.
		You keep working and get the other vikings finish the game with you.
		You get a good night's sleep.
		"""
	if answer == 'N' :
		print"""
		The guy asks you, "WHY NOT", to which you reply, "I am working on my DOPE game."
		He is impressed with your dedication to coding and gives you a high five.
		Your dedication allows you to finish the game within the day
		You get a good night's sleep
		"""
	

def judging():
	print """
	JUDGING!!!!!!
		
		Your dedication has paid off. Your game is a popular hit amongst the judges.
		The judges, however, also want a battle with you to test your skills.(What is up with these battles???)
		
	ROUND 1
		Mike Almond of Race Roster

		Like his company's name suggests, he is a speedster. He challenges you to a SPEED battle.
		Here are your options:
			1 - Run a marathon
			2 - Who can code a DOPE game faster
			3 - Drag race 
			4 - Beer On A Table racing
			(Choose wisely, you only have TWO more people to go!)
				"""
	fight = raw_input('What method? ')
	for case in switch(fight):
		if case('1'):
			print "\n>>Sadly for you, Mike is an experienced runner who has run many marathons"
			print ">> GG you lost."
			print "\n\n\tTRY DIFFERENT COMBINATIONS NEXT TIME!\n"
			judging()
			break
		if case('2'):
			print "\n>>Thanks to your HOURS of experience in coding, you successfully beat Mike"
			print ">>Mike's face is that of defeat. He is bitter."
			print ">>You tell him \"It's okay my man, there's plenty of room to improve\" "
			print ">>You now move on to next round.\n"
			break
		if case('3'):
			print "\n>>You realize you don't have a car."
			print "\n\n\tTRY DIFFERENT COMBINATIONS NEXT TIME!\n"
			judging()
			break
		if case('4'):
			print "\n>>You are underage."
			print ">>No underage drinking please!"
			print "\n\n\tTRY DIFFERENT COMBINATIONS NEXT TIME!\n"
			judging()
			break
		if case(): 
			print "PICK!"
			judging()
	
def Jon():
	print """
	ROUND 2
		Jon Seigel of Application Security Specialist

		Jon has a sly grin on his face. He has been waiting for this moment since hearing about you.
		"YOU THINK YOU CAN DEFEAT ME? JOIN ME IN A MUSIC BATTLE!"
		
		What do you use?
			1 - Clarinet
			2 - Rap
			3 - Bass Guitar
			4 - Harp
			(hINT: I like TO make puns)
		"""
	fight = raw_input('What method? ')
	for case in switch(fight):
		if case('1'):
			print "\n>>Jon is an expert on clarinet. He wins the heart of the audience with his skills"
			print ">> You, on the other hand, know nothing about it except that Squidward plays it"
			print "\n\n\tTRY DIFFERENT COMBINATIONS NEXT TIME!\n"
			Jon()
			break
		if case('2'):
			print "\n>>Thankfully, you have some experience with rapping"
			print ">>You tell the kid next to you to drop the beat"
			print ">>You proceed to drop the firest rap ever written"
			print ">> \\ MIC DROP \\"
			print ">>Jon cries in shame as he disintegrates due to how fire the rap is."
			print ">>You now move on to next round to face the ULTIMATE JUDGE\n"
			break
		if case('3'):
			print "\n>>You pick the bass guitar, despite your only experience with it being playing on Guitar Hero"
			print ">>The crowd boos you off the stage"
			print ">>Jon starts playing. The musical sound of his guitar makes people cry"
			print ">>The guitar also gently weeps becuase it's so happy to be played by Jon"
			print ">>The power of music blows you apart"
			print "\n\n\tTRY DIFFERENT COMBINATIONS NEXT TIME!\n"
			Jon()
			break
			exit()
		if case('4'):
			print "\n>>No one knows how to play the harp"
			print ">>It's a tie!"
			break
		if case(): 
			print "PICK!"
			Jon()

def albert():
	print """
	ROUND 3

	Albert Lai of Big Viking Games
	This is the big moment. What do you do?
		
		1 - Bark like a dog, then punch him
		2 - Sing Led Zepplin's Immigrant Song
		3 - Try to negotiate with him like a reasonable human being
		4 - Give up
		5 - CODING BATTLE!!!!!!!!!!
		
		"""
	fight = raw_input('What: ')
	for case in switch(fight):
		if case('1'):
			print "\n>>Albert is dumbfounded."
			print ">> \' WHAT IS THIS KID DOING????\'"
			print ">>Albert is hella confused. You punch him. He passes out.\n"
			print ">>That was easy!... or was it?"
			break
		if case('2'):
			print "\n>>\"AHHHHHHHHHHHHH AH!!!! AHHHHHHHHH AH!!!!!!\""
			print ">>Every glass within the 10 km radius shatter"
			print ">>Charged with property damage! :("
			print ">>GG"
			print "\n\n\tTRY A DIFFERENT COMBINATION NEXT TIME!\n"
			albert()
			break
		if case('3'):
			print "\n>>You try to talk to Albert like a reasonable human being."
			print ">> HOW DARE YOU TREAT ME LIKE A MORTAL?????"
			print ">> Albert disqualifies you immediately"
			print "\n\n\tTRY A DIFFERENT COMBINATION NEXT TIME!\n"
			albert()
			break
		if case('4'):
			print "You give up."
			print "You embarassed yourself infront of everyone"
			quit()
			break
		if case('5'):
			print "\n>>He wants to code a program to analyze a velocity of a unladen swallow in Ruby on Rails"
			print ">>You have never used that before in your life"
			print ">>Albert proceeds to whoop your butt "
			print ">>GG"
			print "\n\n\tTRY A DIFFERENT COMBINATION NEXT TIME!\n"
			albert()
			break
		if case(): # default, could also just omit condition or 'if True'
			print "PICK!"
			albert()

def albert2():
	print """
	Albert regains consciousness.
	As he slowly rises, the ground begins to shake...
	His hair turns blonde and starts to defy gravity....
	You see an aura glowing around him...
	HE'S GONE SUPER SAIYAN!

	He says in his mighty voice,
	\"YOU FOOOOOOOOOOOOOOL! GET READY TO FACE YOUR DEMISE!!!!!!!!!!!\"

	Options:
	1 - Throw rocks!
	2 - Summon the Great Viking Gods
	3 - Duel him on Smash
	4 - Challenge him to a rap battle
	5 - Challenge him to a naked oiled wrestling match
	6 - Ask him to marry you 
	"""
	final = raw_input('O SHIT!!!!:')
	for case in switch(final):
		if case('1'):
			print "\n>>Rocks deal no damage to #BasedGodAlbert"
			print ">>He's angrier than before"
			print ">> It's not very effective..."
			print "\n\n\tTRY AGAIN"
			albert2()
			break
		if case('2'):
			print "\n>>You proceed to summon the Great Viking Gods"
			print ">>They speak Norwegian to you"
			print ">>WHAT IS GOING ON??????????"
			print ">>It's not very effective..."
			print "\n\n\tTRY AGAIN"
			albert2()
			break
		if case('3'):
			print "\n>>You challnge him to a Smash Duel"
			print ">>It's Melee and he picks Fox against your Kirby"
			print ">>Damn...."
			print ">>You lose, further fueling his ego"
			print ">> It's not very effective..."
			print "\n\n\tTRY AGAIN"
			albert2()
			break
		if case('4'):
			print "\n>>You challenge him to a rap battle"
			print ">>#BasedGodAlber is not #RapGodAlbert"
			print ">>HIS MIXTAPE IS LIT!"
			print "IT'S SUPER EFFECTIVE to YOU!!!"
			print ">> It's not very effective..."
			print "\n\n\tTRY AGAIN"
			albert2()
			break
		if case('5'):
			print "\n>>You challenge him to a naked oiled wrestling match"
			print ">>Albert refuses to participate"
			print ">>GG"
			print ">> It's not very effective..."
			print "\n\n\tTRY AGAIN"
			albert2()
			break
		if case('6'):
			print "\n>>You ask Albert to marry you"
			print ">>Albert says yes"
			print "........"
			break
		if case(): # default, could also just omit condition or 'if True'
			print "PICK!"
			albert2()
			break

def end():
	print """
	Well, things escalated quickly between you and Albert.
	You two are now married.
	You won more than an award at the HackWestern,

	a heart.

	<3

	Thank you for playing the game! 

	S/O to Zedd Shaw for Learn Python the Hardway & my team members Sally, Henry, and Carol!
	
	Please try the game again with different combinations!
	
	
	Developed by Andy Park, hg4park@uwaterloo.ca
	"""


main()
beginning()
afterRegistration()
raw_input("\n\\wHAT'S NEXT?\\")
afterRegistration()
raw_input("\n\\wHAT'S NEXT?\\")
afterRegistration()
raw_input("\n\\Press Enter to continue to the next phase!\\")
afterAfterRegistration()
projects()
working()
working2()
raw_input("\n\\Press Enter to continue...\\")
sleep()
raw_input("\n\\Press Enter to wake up!!!!\\")
day2()
raw_input("\n\\Press Enter to submit your game\\")
judging()
raw_input("\n\\Press Enter to continue to the next round\\")
Jon()
raw_input("\n\\Press Enter to continue to the final judge\\")
albert()
raw_input("\n\\Press Enter to continue... I do not like that \"was it\" part\\ ")
albert2()
raw_input("\nPress Enter to continue & find out more...")
end()