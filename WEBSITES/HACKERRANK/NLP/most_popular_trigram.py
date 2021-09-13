
from collections import defaultdict
def extract_tri(text):
	dict_tri = defaultdict(int)
	listofwords = text.split(' ')
	#print listofwords
	for i in range(0, len(listofwords)):
		try:
			#text = ''.join(listofwords[i:i+4]).strip(' ')
			text = [True if i.isalnum() for i in ''.join(listofwords[i:i+4]).strip(' ')]
			if False in text:
				print "avoid"
				continue
			dict_tri[(listofwords[i], listofwords[i+1], listofwords[i+2])] += 1
		except:
			pass
	#print listofwords
	#sorted_x = dict(sorted(fdist.items(), key=operator.itemgetter(1), reverse=True))
	max_occ = max(dict_tri.values())
	for k,v in dict_tri.items():
		if v == max_occ:
			print k[0] + ' ' + k[1] + ' ' + k[2]









text = raw_input()
text = 'â€œI wish Dave Dashaway would hurry up here,â€ said Hiram Dobbs, who was for the time being in charge of the biplane, the _Comet_. â€œWhatâ€™s your great anxiety, Hiram?â€ questioned Elmer Brackett, reclining
comfortably in one of the spacious seats behind the pilot post of the
machine. â€œDo you know that fellow with the long frock coat over yonderâ€”the one
who looks like some cheap sharp lawyer? There,â€ added Hiram, pointing at
a group near a hangar, â€œheâ€™s talking now with that fat, porpoise-looking
man with gold braid on his cap and a badge on his coat.â€ â€œI see them,â€ nodded young Brackett. â€œNever saw either before that I can
remember. What of them?â€ â€œJust this,â€ replied the young airman, quite seriously. â€œThat lawyer
fellow has been rustling around like a hen on a hot griddle for the last
ten minutes. He seemed to be waiting for someone. Then I saw that man
with the light fuzzy hat, and a moustache and glasses, come in a great
hurry up to him, and direct his attention to the airship here. Just now
the same fellow pointed it out to that constableâ€”policemanâ€”or whatever
he is.â€

â€œI declare!â€ exclaimed Elmer, with a start, sitting up and taking
notice. â€œWhy, I know the man with the fuzzy hat.â€

â€œYou do?â€

â€œI am sure of it, Hiram. He is disguised, but I certainly recognize him.
That fellow is my enemy,â€ and the speaker shifted around in his seat,
greatly disturbed. â€œDo you remember that fellow Vernon?â€

â€œI should say so, and I suspected it to be just that individual all
along,â€ explained Hiram. â€œHeâ€™s made all of us trouble enough not to be
forgotten.â€

â€œI wish Dave would come,â€ said Elmer, anxiously. â€œIt would be a terrible
thing if, after all my hopes and preparations, something should come up
to prevent my going with you on the great airship trip around the
world.â€

Elmer Brackett spoke very earnestly. He might well do so. When he
referred to an exploit that sounded like the scheme of some visionary,
his words had a tangible and sensible business basis.

His companion was pretty nearly a professional airman, and Elmer himself
knew a great deal about aircraft. His father was practically the owner
of the Interstate Aero Company. The person they were now awaiting, Dave
Dashaway, was a youth who had won fame and fortune in the aviation
field.

Young as Dave was, this expert had pretty nearly reached the top as a
professional airman. Those who have been introduced to him in the first
book of the present series, named â€œDave Dashaway, the Young Aviator,â€
will recall with interest his first struggles to earn recognition and a
living in a line to which he was naturally adapted. Dave Dashawayâ€™s
father had been a scientific balloonist, and when Dave met the old
aviator, Robert King, he found a man who was glad to help him on in his
ambition to succeed as a sky sailor.

Dave steadily and earnestly studied aeronautics as if he was learning a
trade. In the second volume of this series, entitled â€œDave Dashaway and
His Hydroplane,â€ the energetic young airman won marked distinction at an
aero meet by his monoplane and hydroplane work. His ability won the
attention of a friend and former professional associate of his father,
and the latter agreed to finance the most stupendous aerial proposition
ever attempted.

The result has been told in the preceding volume of this series called,
â€œDave Dashaway and His Giant Airship.â€ The remarkable adventures of Dave
and his friends while sailing the mammoth airship, the _Albatross_,
across the Atlantic Ocean have there been narrated. After the giant
airship had started on its extraordinary trip, a stowaway had been
discoveredâ€”Elmer Brackett.

It seemed that the lad had gotten into bad company. His father was rich
and he had plenty of money, which he spent very foolishly. He had formed
the acquaintance of a clever schemer named Vernon. This man had so
enmeshed Elmer in his toils, that he made the boy believe that he could
send him to prison, and ruin his fatherâ€™s business. All this was untrue,
but in sheer desperation, believing he had wrecked all his chances in
life, the frightened lad had secretly stolen aboard of the _Albatross_.
In a very heroic way he had saved the crew of the giant airship from
capture by some mountain outlaws in North Carolina, where the
_Albatross_ had descended for repairs. This had made him a welcome
comrade to Dave and Hiram. When the former returned to the United
States, victor in the great race across the Atlantic and the possessor
of a small fortune in prize money, his first task was to hunt up the
schemer, Vernon. Dave gave the rascal to understand that if he annoyed
Elmer any further, he would find himself in serious trouble.

For all that Dave Dashaway and the powerful friends he had made did,
however, Vernon was slow to abandon his hope of fleecing his victim out
of more money. He tried to blackmail Mr. Brackett, and even brought a
suit against the wealthy manufacturer on some notes he had induced the
son to sign under false pretences. To get rid of him, Mr. Brackett had
finally given Vernon a sum of money to cease his annoying persecutions.
Then Vernon had disappeared, and Dave had supposed that he was â€œoff the
mapâ€ for good.

Elmer had acted like a new being since coming under the healthy
influence of the brisk, high-minded young airman, Dave Dashaway, and his
ardent assistant, Hiram Dobbs. For the first time in his life, the zest
of adventure and the ambition to make something of himself had acted
like a spur on the young fellow.

For over a month our hero, Dave, and his two loyal comrades had led an
existence of delight. The young airman had become greatly interested in
an exploit in which he had been invited to take part. The National Aero
Association had arranged for a wonderful novelty and a test in the
aviation field. This was nothing less than an aeroplane race around the
world.

The route had been marked out, the prizes announced and the rules of the
contest adopted. Nearly half a score of contestants had registered. In
the official list there had been published a line or two that the
adventurous Hiram read proudly a dozen times a day: â€œEntrant VIâ€”the
biplane _Comet_, pilot Dave Dashaway.â€

An aero meet was now in progress near the city of Washington, which was
to be the starting point of the great race. Dave and his young
assistants had fairly lived at the plant of the Interstate Aero Company.
Every facility of the great factory had been placed at the command of
Dave. The result had been the construction of the _Comet_, probably the
most perfect and splendid aircraft ever built.

There was a permanent aero practice field near the factory, and on the
afternoon when our story opens the _Comet_ was ready to make its daily
trial flight. With the morrow, entirely equipped and its crew aboard,
the model biplane was to sail across the country for Washington, to be
on hand for the start of the race around the world a few days following.

Other skycraft were in practice or motion about the field. Hiram and
Elmer had gotten their machine in order for a non-stop flight of one
hundred miles. They were waiting for the arrival of Dave, when Hiram
made the discovery that upon the very eve of their grand and stimulating
star exploit, an old enemy had suddenly appeared upon the scene.

Hiram Dobbs bent a keen, suspicious glance at the three men whom he had
pointed out to his comrade. A worried look came into Elmerâ€™s face as he,
too, watched them.

â€œYes,â€ said the latter in an uneasy tone, but convincedly, â€œone of those
men is Vernon.â€

â€œAnd the others are a lawyer and an officer of the law,â€ added Hiram.
â€œThereâ€™s something afoot, Elmer. I guess what it is andâ€”Iâ€™ll fool them.â€

â€œThe constable is coming this way!â€ exclaimed Elmer, apprehensively.

â€œHe wonâ€™t get here quick enough,â€ declared Hiram. â€œI see through their
tricksâ€”Vernon is bent on having you arrested on some flimsy charge. The
scoundrel counts on the belief that your father will pay him more money
rather than see the _Comet_ delayed for the race. Weâ€™ll disappoint him.â€

The speaker shot out his hand to the wheel. His foot was ready to
depress the self-starter button.

â€œAll clear?â€ he called to the field man who stood close by, and the
latter nodded and waved his hand.

â€œThe constable is running towards us,â€ said Elmer rapidly.

Chug! chug! The _Comet_ rose from the ground. Elmer Brackett uttered a
great sigh of relief. Hiram chuckled softly to himself.

â€œHold on! Iâ€™ve got a warrant! In the name of the lawâ€”ugh!â€

The _Comet_ gave a great sway. Its pilot dared not relax attention to
his duties, but he shot a swift glance at the source of the outcry.

â€œThe mischief!â€ uttered Hiram, in surprise and concern.

The big bulky constable was clinging to the machine body, his feet
dangling, his face white and scared-looking, swaying helplessly except
for his frantic hand-hold fifty feet above the ground!'
extract_tri(text)