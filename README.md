# Icebox Breakfast Bot

This is a simple Mastodon bot, written in response to Mark Sample's excellent
[Just To Say Bot](https://twitter.com/justtosaybot). The words that Mark's bot
switches out in its generative process, this bot retains, and vice-versa. I
made this as an experiment, to see why Mark's poetic and procedural choices
mattered when he made his bot. What I discovered: Mark's implementation
highlights the original poem's anti-capitalist underpinnings, evident in the
narrator's begging forgiveness for unwelcome exploitation. My bot, on the other
hand, is about all the whimsical scenarios you can think up about plums,
iceboxes and breakfasting.

Experiment: Success!

I decided to put this bot on Mastodon, rather than Twitter, because its outputs
are routinely longer than 140 characters, and I was too lazy to use PIL or
something to composite an image. Also, I wanted to try to make a Mastodon bot.

[Follow the bot here.](https://botsin.space/@iceboxbreakfast)

## Implementation

The core of this program are the lists of verbs (`*_lemmas.txt` in this
repository) which are extracted from WordNet by searching for verbs with frames
matching that of the original verb in the poem. This ensures a fundamental
semantic similarity between the randomly-selected verb and the verb it replaces
in the poem. A number of other, smaller word lists contribute to the program's
lexicon (including a `prepositions.json` file later submitted to Corpora
Project).

The `complete_conjugation()` function in `generate.py` uses Pattern's
`conjugate()` function to produce a conjugated verb phrase (potentially
incorporating an adverb), including the necessary auxiliary verbs, in
past/present/future tenses and perfect/progressive aspects. The `generate()`
function glues everything together using an elaborate template.

## The Bot

The portion of the program that posts to Mastodon uses
[Mastodon.py](http://mastodonpy.readthedocs.io/en/latest/). [I've written an
account/tutorial of obtaining credentials with Mastodon.py
here](https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26). All
the bot does is read the credentials from the command line, run the
`generate()` function, and post the resulting string. Simple!

## License

The source code in this repository is provided under the MIT license. See LICENSE.TXT for more information. The contents of `*_lemmas.txt` are derived from WordNet, and carry the following license:

WordNet 3.0 license: (Download)

WordNet Release 3.0 This software and database is being provided to you, the
LICENSEE, by Princeton University under the following license. By obtaining,
using and/or copying this software and database, you agree that you have read,
understood, and will comply with these terms and conditions.: Permission to
use, copy, modify and distribute this software and database and its
documentation for any purpose and without fee or royalty is hereby granted,
provided that you agree to comply with the following copyright notice and
statements, including the disclaimer, and that the same appear on ALL copies of
the software, database and documentation, including modifications that you make
for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton
University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS"
AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO
REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY
PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR
DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS
OR OTHER RIGHTS. The name of Princeton University or Princeton may not be used
in advertising or publicity pertaining to distribution of the software and/or
database. Title to copyright in this software, database and any associated
documentation shall at all times remain with Princeton University and LICENSEE
agrees to preserve same.
