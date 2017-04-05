import random
from random import choice as ch
import json

import pattern
from pattern.en import conjugate, PAST, PARTICIPLE, SG, PL

prepositions = json.load(open("prepositions.json"))['prepositions']

def ucfirst(s):
    return s[0].upper() + s[1:]

def complete_conjugation(verb, person, number, tense, aspect, adv=None):
    """
        present None: I eat, you eat ...
        present perfect: I have eaten, you have eaten ...
        present progressive: I am eating, you are eating...
        past None: I ate, you ate ...
        past perfect: I had eaten, you had eaten ...
        past progressive: I was eating, you were eating ...
        future None: I will eat, you will eat ...
        future perfect: I will have eaten, you will have eaten ...
        future progressive: I will be eating, you will be eating ...
    """
    vals = {
        ('present', None): lambda: "%s" % conjugate(verb, person=person,
            number=number),
        ('present', 'perfect'): lambda: "%s %s" % (conjugate('have',
            person=person, number=number), conjugate(verb, PAST+PARTICIPLE)),
        ('present', 'progressive'): lambda: "%s %s" % (conjugate('be',
            person=person, number=number), conjugate(verb, PARTICIPLE)),
        ('past', None): lambda: "%s" % conjugate(verb, person=person,
            number=number, tense=PAST),
        ('past', 'perfect'): lambda: "%s %s" % (conjugate('have', person=person,
            number=number, tense=PAST), conjugate(verb, PAST+PARTICIPLE)),
        ('past', 'progressive'): lambda: "%s %s" % (conjugate('be',
            person=person, number=number, tense=PAST), conjugate(verb,
                PARTICIPLE)),
        ('future', None): lambda: "will %s" % verb,
        ('future', 'perfect'): lambda: "will have %s" % conjugate(verb,
            PAST+PARTICIPLE),
        ('future', 'progressive'): lambda: "will be %s" % conjugate(verb,
            PARTICIPLE)
    }
    output = vals[(tense, aspect)]()
    # how to teach a computer syntax, chapter one
    if adv is not None:
        if len(output.split()) > 1:
            output = " ".join(output.split()[:1] + [adv] + output.split()[1:])
        else:
            output = adv + " " + output
    return output

def generate(verbs):
    subj_pron = {
        'I': (1, SG),
        'we': (1, PL),
        'you': (2, SG),
        'you': (2, PL),
        'he': (3, SG),
        'she': (3, SG),
        'it': (3, SG),
        'they': (3, PL)
    }
    obj_pron_imp = ['me', 'us', 'yourself', 'him', 'her', 'them']

    tenses = ['present', 'past', 'future']
    aspects = [None, 'perfect', 'progressive']

    determiners_sg = [
        'the', 'this', 'an', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'every', 'no'
    ]

    determiners_pl = [
        'the', 'these', 'some', 'no', 'a few of the', 'both', 'all of the'
    ]

    dem_pronouns = [
        ('this', SG), ('that', SG), ('these', PL), ('those', PL)
    ]

    rel_pronouns_subj = ['that', 'which', 'who']
    rel_pronouns_obj = ['that', 'which', 'whom']

    conjunctions = ['and', 'but', 'or']

    justs = [
        "merely",
        "simply",
        "only",
        "but",
        "exactly",
        "precisely",
        "barely",
        "hardly",
        "scarcely",
        "solely"
    ]

    adverbs = [
        "duly",
        "decidedly",
        "equally",
        "fitly",
        "suitably",
        "awfully",
        "especially",
        "extra",
        "oddly",
        "peculiarly",
        "plenty",
        "really",
        "remarkably",
        "right",
        "strangely",
        "terribly",
        "terrifically",
        "too",
        "uncommonly",
        "very",
        "overly"
    ]

    return """%(this_is)s %(just)s To %(Say)s

%(I_have_eaten)s
%(the1)s plums
%(that)s were %(in)s %(the2)s icebox

%(and1)s %(which)s
%(you_were_probably_saving)s
%(for)s breakfast

%(Forgive)s %(me)s
%(they_were)s delicious
%(so1)s sweet
%(and2)s %(so2)s cold""" % {
        'this_is': (lambda x: x[0] + " " + complete_conjugation('be', 3, x[1],
            ch(tenses), ch([None, 'perfect'])))(ch(dem_pronouns)).title(),
        'just': ucfirst(ch(justs)),
        'Say': ucfirst(ch(verbs['say'])),
        'I_have_eaten': (lambda x:
            ucfirst(x[0]) + " " + complete_conjugation(ch(verbs['eat']),
                x[1][0], x[1][1], ch(tenses),
                ch(aspects)))(ch(subj_pron.items())),
        'the1': ch(determiners_pl),
        'that': ch(rel_pronouns_subj),
        'in': ch(prepositions),
        'the2': ch(determiners_sg),
        'and1': ch(conjunctions),
        'which': ch(rel_pronouns_obj),
        'you_were_probably_saving': (lambda x:
            x[0] + " " + complete_conjugation(ch(verbs['save']), x[1][0],
            x[1][1], ch(tenses), ch(aspects),
            adv="probably"))(ch(subj_pron.items())),
        'for': ch(prepositions),
        'Forgive': ucfirst(ch(verbs['forgive'])),
        'me': ch(obj_pron_imp),
        'they_were': (lambda x: x[0] + " " + complete_conjugation('be',
            x[1][0], x[1][1], ch(tenses),
            ch([None, 'perfect'])))(ch(subj_pron.items())),
        'so1': ch(adverbs),
        'and2': ch(conjunctions),
        'so2': ch(adverbs)
}

def main():
    verbs = dict()
    verbs['say'] = [x.strip() for x in open("say_lemmas.txt").readlines()]
    verbs['eat'] = [x.strip() for x in open("eat_lemmas.txt").readlines()]
    verbs['save'] = [x.strip() for x in open("save_lemmas.txt").readlines()]
    verbs['forgive'] = [x.strip() for x in
            open("forgive_lemmas.txt").readlines()]
    for i in range(50):
        print "---"
        print generate(verbs)
        print ""
        print ""

if __name__ == '__main__':
    main()

