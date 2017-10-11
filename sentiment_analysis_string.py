#!/usr/bin/env python3

from wnaffect import WNAffect
wna = WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
import nltk
from nltk.tokenize import RegexpTokenizer

def senti_analysis(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    story = nltk.pos_tag(tokens)
    emotion_story = []
    for word, pos in story:
        emo = wna.get_emotion(word, pos)
        if emo == None:
            continue
        else:
            root_emotion = ' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)])
            emotion_story.append(root_emotion)

    pos, neg, ambi = 0, 0, 0
    for i in emotion_story:
        if 'positive' in i:
            pos += 1
        elif 'negative' in i:
            neg += 1
        elif 'ambiguous' in i:
            ambi += 1

    verdict = ""
    if (pos >= 4 and neg >= 4) and (neg - pos <= 7 and neg - pos >= -7):
        verdict = "Controversial"
    elif (pos < 2 or neg < 2):
        verdict = "Not Enough Data"
    else:
        verdict = "Not Controversial"
    return verdict, str(pos), str(neg), str(ambi)

# a = senti_analysis("Is helpless outrage the only choice gun-control advocates have after Las Vegas? As the horrific news unfolded, share prices of major gun manufacturers rose. Market investors were trading on the ugly reality we all knew: Gun regulations would not change, but fear of them would drive sales.Understanding the choices gun-control advocates have begins with understanding where the outsize power of the National Rifle Association originates.Most people assume its power comes from money. The truth is that gun-control advocates have lots of money, too. Billionaires like Michael Bloomberg have pledged fortunes to supporting gun control. After mass shootings, support for sensible gun laws grows.The N.R.A.’s power is not just about its money or number of supporters or a favorable political map. It has also built something that gun-control advocates lack: an organized base of grass-roots power.I grew up in Texas and now live in California. I study grass-roots organizations. I am a gun-control advocate with childhood friends who are ardent gun-rights supporters. I have seen the different ways in which the gun-rights and gun-control movements have built their bases.First, gun-control groups summon action among people who agree, while gun-rights groups engage people who do not necessarily agree in association with one another. Most people assume that people who join groups like the N.R.A. are people who support gun rights — but that is not always the case.Consider the anti-abortion movement. The sociologist Ziad Munson has found that almost half of the activists on the front lines of the anti-abortion movement — those who protest outside abortion clinics — were not anti-abortion when they attended their first event. They attended because a friend asked them, they had just joined a new church, or they retired and had more free time. They stayed, however, because at these events, they found things we all want: friends, responsibility, a sense that what they are doing matters. By finding fellowship and responsibility, these people changed not only their views on abortion but also their commitment to act.Local gun clubs and gun shops provide a similar structure for the gun-rights movement. There are more gun clubs and gun shops in the United States than there are McDonald’s. (The proportion of gun clubs affiliated with the N.R.A. is notoriously hard to track.) My friends who support the N.R.A. did not join a club because of politics. They joined because they wanted somewhere to shoot their guns.The base of the gun-control movement is defined not by clubs but by ideology: people who come to the movement and share a view on gun control and can be sent into action. The organizations then add up those actions to claim a base. We take it for granted that gun-control groups have to define their base by moral outrage. The truth is, it’s a choice that movement leaders make. They can decide to work through structures or not.Second, gun-control groups focus on persuasion, while gun-rights groups focus on identity. In many ways, my friends and I who disagree on guns are similar. But their views evolved after joining these gun groups. So did their identities. The gun-rights groups were not just persuading them to support gun rights; they were also helping my friends rearticulate their own lives in terms of a broader vision of the future. They were no longer just hunters. They were protectors of a way of life. That is why the N.R.A.’s version of gun rights is so intimately tied to questions of race and identity.When I joined gun-control groups, I got messages about narrowly defined issues like background checks and safety locks. These messages were a pollster’s dream, tested down to the comma to maximize the likelihood that I would donate or take action. But they never challenged me to rethink who I was or what my relationship to my community was.Third, for gun-rights groups, the work of engaging with identity and getting people to associate rests on a choice leaders made to invest in building the capacity of ordinary people to participate — and lead — in politics. When I studied groups that were most effective at building a grass-roots base, I found that the key factor to success was the nature of the relationships they created. The most effective groups used relationships as a vehicle for bringing people off the sidelines of public life and teaching them to speak truth to power. You can’t convince someone to rethink who they are or what responsibility they want to take for their community through a mailer.I have two young children. After Sandy Hook, I joined several gun-control organizations in a desperate effort to do something. These organizations asked me for money and sent me links for places to send emails or make phone calls. But none introduced me to anyone else in the organization or invited me to strategize about what I could do. Instead, I felt like a prop in a game under their control. I eventually asked to be taken off their lists.Many groups, like Everytown for Gun Safety, are doing vital work to build a movement in the face of the entrenched power of the N.R.A. Reform will take more than raising money or shifting public opinion. The currency that matters in grass-roots power is commitment.Elected officials can recognize the difference between organizations that can activate only people who are in agreement and those that can transform people who are not. The N.R.A. got over 80,000 people from all over the country to attend its annual meeting in 2017. What gun-control organization can claim the same?Building a movement will require organizations to invest in the leadership of ordinary people by equipping them with the motivations, skills and autonomy they need to act. Most organizations never give people that opportunity.Since the 2016 election, we have seen people engaged and hungry for the opportunity to take meaningful action. The question is, will one of the deadliest shootings of Americans in United States history prompt gun-control leaders to give people that chance?")
#
# print(a)

