#text = 'In dealing with this period they sternly condemn the historical personages who, in their opinion, caused what they describe as the reaction. All the well-known people of that period, from Alexander and Napoleon to Madame de Stael, Photius, Schelling, Fichte, Chateaubriand, and the rest, pass before their stern judgment seat and are acquitted or condemned according to whether they conduced to progress or to reaction.  According to their accounts a reaction took place at that time in Russia also, and the chief culprit was Alexander I, the same man who according to them was the chief cause of the liberal movement at the commencement of his reign, being the savior of Russia.  There is no one in Russian literature now, from schoolboy essayist to learned historian, who does not throw his little stone at Alexander for things he did wrong at this period of his reign. What do these reproaches mean?  Do not the very actions for which the historians praise Alexander I (the liberal attempts at the beginning of his reign, his struggle with Napoleon, the firmness he displayed in 1812 and the campaign of 1813) flow from the same sources--the circumstances of his birth, education, and life--that made his personality what it was and from which the actions for which they blame him (the Holy Alliance, the restoration of Poland, and the reaction of 1820 and later) also flowed?  In what does the substance of those reproaches lie?  It lies in the fact that an historic character like Alexander I, standing on the highest possible pinnacle of human power with the blinding light of history focused upon him; a character exposed to those strongest of all influences: the intrigues, flattery, and self-deception inseparable from power; a character who at every moment of his life felt a responsibility for all that was happening in Europe; and not a fictitious but a live character who like every man had his personal habits, passions, and impulses toward goodness, beauty, and truth--that this character--though not lacking in virtue (the historians do not accuse him of that)--had not the same conception of the welfare of humanity fifty years ago as a present-day professor who from his youth upwards has been occupied with learning: that is, with books and lectures and with taking notes from them. "What a woman--oh, what a woman!" cried the King of Bohemia, when we had all three read this epistle.  "You could not possibly have come at a better time, my dear Watson," he said cordially. \'It is not worth your while to wait,\' she went on. \'You can pass through the door; no one hinders.\' And then, seeing that I smiled and shook my head, she suddenly threw aside her constraint and made a step forward, with her hands wrung together.'
#from nltk.tokenize import sent_tokenize

import re
def splitParagraphIntoSentences(paragraph):

	#sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',paragraph)
	#for s in sent:
	#	print s 

	indices = []
	l = []
	p = re.compile("(\.|\?|\!)\s*")
	for m in p.finditer(paragraph):
		try:
			if paragraph[int(m.start())+1] not in ['"']:
				indices.append(m.start())
		except:
			pass

	j = 0
	for i in indices:
		l.append(paragraph[j: i+1])
		j = i+1 

	sent = [i.lstrip(' ').rstrip(' ') + '\n' for i in l]
	sent = ''.join(sent)
	return sent.rstrip('\n')
	'''

	

	paragraph = paragraph.replace('?', '. ')
	paragraph = paragraph.replace('!', '. ')

	paragraph = paragraph.replace('  ', ' ')
	sent_tokenize_list = sent_tokenize(paragraph)
	sent = [i+'\n' for i in sent_tokenize_list]
	sent = ''.join(sent)
	return sent.rstrip('\n')
	'''

text = raw_input()

print splitParagraphIntoSentences(text)
