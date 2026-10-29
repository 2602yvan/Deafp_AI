import random
import pyttsx3



def generate_happy_phrase(text: str) -> str:
    openers = [
        "With a grin,", "Laughing a little,", "Smiling wide,", "Beaming with joy,", "Eyes sparkling,",
        "In a good mood,", "With cheeks glowing,", "Radiating warmth,", "Almost dancing,",
        "With sunshine in their voice,", "With joy in their step,", "Grinning from ear to ear,",
        "Eyes twinkling,", "With a voice like a hug,", "Cheeks lifted in a smile,",
        "With a skip in their voice,", "Sunshine dancing in their words,", "Humming to themselves,",
        "With laughter in their breath,", "Buzzing with good vibes,", "With pure delight in their tone,",
        "Practically glowing,", "With happiness oozing from every word,", "Grinning like a kid with candy,",
        "Overflowing with giddiness,", "As if walking on sunshine,", "With a joy they couldn’t hide,",
        "Bubbling with excitement,", "Smiling like they just heard the best news,", "With a heart full of light,"
    ]

    verbs = [
        "they said", "they giggled", "they chuckled", "they admitted", "they confessed", "they sang",
        "they shared", "they beamed", "they whispered playfully", "they teased"
    ]

    flairs = [
        "like it was a secret they couldn’t keep", "as if their heart couldn’t contain it",
        "like joy was bubbling out", "like the words tasted sweet", "with a little hop in their tone",
        "like they were wrapped in sunlight", "without a care in the world", "with playful charm",
        "like a melody was in the air", "and it felt like summer in a sentence",
        "like their smile reached their voice", "as if the world had just told them a joke",
        "like happiness came pouring out", "with the giddiness of a child at recess",
        "like the sky cleared just for them", "as if the moment was too sweet to hold back",
        "like laughter was stitched into the words", "like the sun had kissed their thoughts",
        "like they’d waited all day to say it", "with a sparkle in their voice",
        "like it slipped out with sunshine", "as if they were dancing on air",
        "with that pure kind of joy", "like the words skipped out of their mouth",
        "as if their soul was beaming", "like it was dipped in honey",
        "as if nothing else mattered", "like it made their whole day",
        "with a skip in their sentence", "as if their heart was doing cartwheels",
        "like it was written in the stars", "as if they'd burst if they didn’t say it",
        "with a grin tucked in each word", "like it was music to their own ears",
        "with that unmistakable happy tone", "like they were hugging the moment",
        "as if sunshine was speaking through them", "like their joy needed to be heard",
        "with warmth that filled the room", "like it was the easiest thing to say",
        "as if life felt lighter in that moment", "with a tone as soft as laughter",
        "like every word was a celebration", "as if their mood was contagious",
        "like they couldn’t help themselves", "with that wide-eyed wonder",
        "as if they were bubbling with affection", "like a hug hidden in a sentence",
        "with cheer wrapped around each syllable", "as if joy had a voice",
        "like the world had just smiled at them", "as if their chest was glowing",
        "like each word wore a party hat", "with sunshine stitched into the sentence",
        "as if the wind whispered it first", "like they were high on happiness",
        "with the ease of a breeze", "as if nothing could go wrong",
        "like their heart was singing", "as if the moment was dipped in joy"
    ]

    opener = random.choice(openers)
    verb = random.choice(verbs)
    flair = random.choice(flairs)

    return f"{opener} {verb}, \"{text}\" — {flair}."


def generate_sad_sentence(text: str) -> str:
    # Provided lists
    openers = [
        "Sounding a little off,", "Like something was weighing on them,", "In a quiet tone,",
        "Voice barely above a whisper,", "Trying to keep it together,", "With a slow exhale,",
        "Sounding distant,", "Like they weren’t really present,", "With a bit of hesitation,",
        "Speaking slower than usual,", "Almost holding back,", "Like something was stuck in their chest,",
        "Voice dull,", "Sounding not quite okay,", "With a small frown,", "Like they’d rather not say it,",
        "Trying not to let it show,", "A bit choked up,", "Fighting to sound normal,",
        "Like the words were hard to say,", "Taking a pause before speaking,",
        "Voice low and careful,", "With a kind of tiredness,", "Not quite meeting your gaze,",
        "Like it cost them something to say it,", "Trying to sound okay but not quite,",
        "After a moment of silence,", "Like their thoughts were somewhere else,",
        "Sounding unsure,", "Dragging the words out,", "With a slow nod,",
        "Just above a breath,", "With tired eyes,", "Like they weren’t ready to talk,",
        "Like they’d been holding it in,", "With a tone that didn’t match the words,",
        "Trying to be casual, but you could hear it,", "Like it slipped out without meaning to,",
        "Sounding like they'd said it before,", "Trying to shrug it off,",
        "With a tired laugh,", "Like they didn’t expect a reply,", "As if they were done pretending,",
        "A bit quieter than normal,", "After clearing their throat,",
        "With a look that said more than the words,", "With less energy than usual,",
        "Like their mind was elsewhere,", "Trying to sound fine,", "As if it had been on their chest for a while,"
    ]

    verbs = [
        "they murmured", "they whispered", "they admitted softly", "they said quietly",
        "they confessed", "they recalled", "they spoke gently", "they uttered",
        "they choked out", "they shared with hesitation"
    ]

    flairs = [
        "like their words were carrying memories", "as if each syllable hurt a little",
        "like sorrow sat in their voice", "with pain hidden between the lines",
        "as though they were holding back tears", "like their heart ached quietly",
        "as if joy had long left", "like they were talking through rain",
        "as though they were tired of pretending", "with silence echoing after every word",
        "like grief curled around each word", "as if the sentence was stitched from pain",
        "like the moment weighed them down", "as if they were speaking from a scar",
        "like hope had stepped away", "with a shadow in their tone",
        "like each word needed effort", "as though their soul was tired",
        "like their voice was fading too", "as if something broke inside",
        "with a hush that said too much", "like the light had dimmed in their world",
        "as if their heart still lingered somewhere else", "like they were unraveling inside",
        "as if they'd said it a hundred times in their head", "with the ache of remembering",
        "as if they were begging to be understood", "like tears were hiding in the breath",
        "as though they'd lost something sacred", "with the quiet ache of longing",
        "as if the world moved without them", "like goodbye had settled in their chest",
        "with the weight of what wasn’t said", "like their words knew sorrow too well",
        "as though their past whispered along", "with the tremble of a held-back cry",
        "like sadness held their tongue", "as if it hurt just to remember",
        "with the ghost of a smile long gone", "like the sentence had cracks in it",
        "as if they wanted to disappear", "with a silence that screamed inside",
        "like the joy had been forgotten", "as if they were waiting for healing",
        "with the quiet of someone hurting", "like time moved too slow for them",
        "as if they didn’t expect to be heard", "with a voice too tired to lie",
        "as if love had left them cold", "like the words were saying goodbye"
    ]

    opener = random.choice(openers)
    verb = random.choice(verbs)
    flair = random.choice(flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'


def generate_angry_sentence(text: str) -> str:
    angry_openers = [
        "With a sharp breath,", "Voice rising,", "Clearly annoyed,", "With clenched teeth,",
        "Almost growling,", "Eyes narrowed,", "Trying to stay calm,", "With a scoff,",
        "With tension in their tone,", "Like they'd had enough,", "With heat in their voice,",
        "Almost biting the words,", "With clear frustration,", "Spitting the words out,",
        "With a sarcastic laugh,", "Rolling their eyes,", "Like fire behind the words,",
        "Voice tight with anger,", "Through gritted teeth,", "Like a storm was coming,",
        "Sounding barely in control,", "With a dry tone,", "With a burst of irritation,",
        "Like their patience had snapped,", "Like they’d been holding this in,",
        "Words hitting hard,", "In a clipped tone,", "Trying not to explode,",
        "With eyes flashing,", "Sounding deeply pissed,", "With fists clenched,",
        "Like they were sick of repeating it,", "With a tone full of venom,",
        "Snapping,", "With a frustrated sigh,", "Like they were done being polite,",
        "Words coming fast,", "Cutting through the moment,", "Like fire in their chest,",
        "In a warning tone,", "Sounding ready to argue,", "Like it was personal now,",
        "Bitterly,", "With no attempt to hide it,", "In a rough tone,",
        "Letting the anger slip out,", "Voice laced with sarcasm,", "With a hard look,",
        "Like they'd had enough of the nonsense,", "Without filtering their tone,",
        "With a voice that dared you to respond,"
    ]
    angry_verbs = [
        "they snapped", "they spat", "they barked", "they hissed",
        "they growled", "they said, biting each word", "they retorted",
        "they demanded", "they lashed out", "they thundered"
    ]
    angry_flairs = [
        "like their patience had just run out",
        "as if they'd been pushed too far",
        "with every word like a strike",
        "like the words were loaded",
        "as though anger was the only thing holding them together",
        "with heat rising behind the words",
        "as if fury shaped the sentence",
        "like the silence before an explosion",
        "as if they'd been simmering all day",
        "with rage tucked behind each syllable",

        # more layered and realistic expressions
        "like they didn’t care who heard",
        "with a storm brewing in their chest",
        "as if they were one second from losing it",
        "like fire under the surface",
        "as if holding back would make it worse",
        "like they'd said it too many times before",
        "with resentment soaked in every word",
        "like they were tired of pretending to be calm",
        "as if their anger had been waiting",
        "like each word was cutting loose",
        "like the words were thrown, not spoken",
        "with bitterness crawling through their tone",
        "as though they'd rehearsed this fight",
        "with zero filter left",
        "as if they'd been insulted one time too many",
        "with fire in every syllable",
        "as if their blood was boiling",
        "like they’d waited too long to say it",
        "with fury they couldn’t mask",
        "like the words were a weapon"
    ]
    opener = random.choice(angry_openers)
    verb = random.choice(angry_verbs)
    flair = random.choice(angry_flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'


def generate_fear_sentence(text: str) -> str:
    fear_openers = [
        "With wide eyes,", "Looking over their shoulder,", "Almost shaking,", "Voice trembling,",
        "With a nervous glance,", "Like something was creeping up behind,", "Barely breathing,",
        "With panic in their voice,", "As if they expected something to go wrong,",
        "With a flinch in their tone,", "Heart racing,", "With unease,", "With a jumpy tone,",
        "With hands clenched tight,", "As if bracing for something,", "With hesitation,",
        "Stammering slightly,", "Like fear had gripped their throat,", "Barely audible,",
        "In a voice not quite steady,", "Eyes darting around,", "Voice cracking a little,",
        "As if unsure they should say it,", "With creeping doubt,", "Almost whispering for safety,",
        "Trying to sound braver than they felt,", "Voice breaking,", "With urgency but fear,",
        "Like they couldn’t believe what they were saying,", "With a warning tone,",
        "Voice sharp with panic,", "With the energy of a held scream,", "Whispers fast and tense,",
        "In a quiet rush,", "Like they were afraid to be heard,", "With nervous energy,",
        "Like something was watching,", "With a pale expression,", "With breath held,",
        "Like their nerves were fraying,", "In a voice that begged for reassurance,",
        "With doubt curled in every word,", "With the edge of fear,", "Like their instincts screamed stop,",
        "As if shadows spoke through them,", "With an air of dread,", "With barely suppressed panic,",
        "With the chill of danger,", "With a lump in their throat,", "With paranoia in their tone,"
    ]

    fear_verbs = [
        "they stammered", "they gasped", "they whispered quickly", "they said under their breath",
        "they blurted out", "they mumbled", "they confessed with tension",
        "they said in a panic", "they uttered with urgency", "they warned"
    ]

    fear_flairs = [
        "like danger was in the room", "as though they were being watched",
        "like the walls were closing in", "with tension tight as a wire",
        "as if something was lurking nearby", "like their breath might give them away",
        "as though they weren’t sure they were safe", "with fear bleeding into every word",
        "like the dark had teeth", "like the silence wasn’t empty",
        "as though their voice might attract something", "like they were waiting to run",
        "with the air of someone hunted", "as if they wanted to vanish",
        "like the words betrayed them", "as if every sound was a risk",
        "with their heart thudding in their voice", "like their thoughts raced too fast",
        "like trust had abandoned them", "with a sense of looming danger",
        "as if they weren’t alone", "like the shadows were alive",
        "as though fear sat on their shoulders", "with panic buried under each syllable",
        "like their courage was slipping", "as if the floor might disappear",
        "like hope was too far away", "with their nerves worn thin",
        "like a scream was waiting to break through", "as though each word cost them safety",
        "like they didn’t want to hear their own voice", "as if their instincts were screaming",
        "like the moment was teetering", "with a voice full of 'what if'",
        "as if one wrong word would break everything", "with eyes full of alarms",
        "like breath was running out", "as if they’d seen too much",
        "with urgency that didn’t feel brave", "like fear made decisions for them",
        "as if the dark held secrets", "like safety was only an idea",
        "with danger stitched in their tone", "as though something was just out of sight",
        "with the stillness before a scream", "like silence was louder than sound",
        "as if the truth was too terrifying", "like fear had become their language",
        "with footsteps echoing in their mind", "as though their thoughts trembled too"
    ]
    opener = random.choice(fear_openers)
    verb = random.choice(fear_verbs)
    flair = random.choice(fear_flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'


def generate_surprise_sentence(text: str) -> str:
    surprise_openers = [
        "With wide eyes,", "In a startled gasp,", "With a sudden jolt,", "In disbelief,", "Almost laughing,",
        "With raised brows,", "Mouth slightly open,", "Blinking quickly,", "With a sharp inhale,", "In shock,",
        "Stunned for a moment,", "With a surprised chuckle,", "With a hand to their chest,", "Eyes bright with wonder,",
        "With a quick double-take,", "With a voice full of wonder,", "Caught completely off-guard,", "Almost shouting,",
        "With astonishment,", "Like they couldn’t believe it,", "With unexpected joy,", "Suddenly excited,",
        "With a rush of realization,", "Eyes wide as saucers,", "With a sudden laugh,",
        "Like lightning struck their thoughts,",
        "With awe in their voice,", "Nearly dropping everything,", "With a sudden grin,", "With total surprise,",
        "Like a gift had fallen from the sky,", "Like their brain had to catch up,", "With a blink and a gasp,",
        "Like it came out of nowhere,", "Like magic had just happened,", "As if they won the lottery,",
        "With a jump of excitement,", "With disbelief turning to joy,", "In a tone of pure amazement,",
        "With wonder in every word,", "Like they didn’t expect to say it,", "As if the world just flipped,",
        "With sudden brightness,", "Like they were hit by clarity,", "With gleeful shock,",
        "With cheeks flushing from surprise,",
        "Like they just discovered something,", "With unexpected delight,", "With eyebrows raised high,",
        "With words tumbling out before they could think,"
    ]

    surprise_verbs = [
        "they exclaimed", "they gasped", "they blurted out", "they laughed nervously", "they said wide-eyed",
        "they burst out", "they squeaked", "they repeated, stunned", "they asked in disbelief", "they marveled"
    ]

    surprise_flairs = [
        "as if they just won something", "like their world just flipped", "as if fate threw them a curveball",
        "with energy jumping off their voice", "like they uncovered a secret", "like it hit them all at once",
        "as if the air had changed", "like they were waking from a dream", "with stunned joy",
        "like they couldn’t quite process it", "with brightness breaking through",
        "like they'd stepped into a new reality", "as if the universe answered them",
        "with wonder they couldn’t hide", "like the impossible just happened",
        "with disbelief fighting a smile", "as if it changed everything",
        "like the stars had realigned", "as if they stumbled on something magical",
        "with a spark in their voice", "like they'd been handed a miracle",
        "with the thrill of the unexpected", "like a puzzle suddenly solved",
        "as if every nerve lit up", "like their breath had caught up to their joy",
        "with amazement dancing behind the words", "like truth had just struck",
        "as if they touched wonder", "like they almost couldn’t believe it",
        "with joy and shock blending together", "like reality had just shifted",
        "as if lightning ran through the moment", "like their heartbeat skipped",
        "with stunned brightness", "like awe broke through", "as if every doubt vanished",
        "like the answer had appeared", "with sudden clarity", "like the sky opened up",
        "with the charm of surprise", "like their eyes had never seen this",
        "as if time paused for wonder", "with every word glowing", "like a new world just began",
        "with dazed happiness", "like disbelief had turned sweet", "as if laughter saved the moment",
        "with magic blooming in their voice", "like it was too good to be true",
        "like joy had snuck up on them"
    ]
    opener = random.choice(surprise_openers)
    verb = random.choice(surprise_verbs)
    flair = random.choice(surprise_flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'


def generate_disgust_sentence(text: str) -> str:
    disgust_openers = [
        "With a scrunched nose,", "Eyebrows furrowed,", "With clear revulsion,", "Voice laced with disdain,",
        "With a sour expression,", "As if they’d just tasted something awful,", "With lips curled back,",
        "Like the words themselves were unpleasant,", "With visible discomfort,",
        "In a tone heavy with disapproval,", "As if holding back a gag,", "With eyes narrowing,",
        "Like something turned their stomach,", "With a huff of disgust,", "Almost recoiling,",
        "With thinly veiled contempt,", "With a twitch of the lip,", "In a grimace,", "With biting tone,",
        "Like every syllable tasted bad,", "With a look of distaste,", "With breath short and sharp,",
        "As if trying not to look,", "With subtle repulsion,", "With a dry scoff,",
        "With a tone that spat the words,", "With their nose slightly wrinkled,",
        "Like it physically pained them to say it,", "With a sound of utter dislike,",
        "In a gritted voice,", "With sarcasm soaked in disgust,", "With eyes squinting in revulsion,",
        "Like they were trying not to vomit,", "With a bitter expression,",
        "With a tongue bitten to hold back worse,", "With barely contained nausea,",
        "As though repelled by the thought,", "With clenched jaw,", "With their face twisted,",
        "With a sneer,", "With the tone of someone offended,", "With their mouth twisted in dismay,",
        "Like bile rose with each word,", "With evident recoil,", "With a wince,",
        "As if trying to unhear the thought,", "With vocal distaste,", "With visible cringing,",
        "Like they hated even repeating it,", "In a clipped and cold voice,"
    ]

    disgust_verbs = [
        "they muttered", "they spat out", "they sneered", "they said sharply", "they scoffed",
        "they murmured with disdain", "they snapped", "they hissed", "they grumbled", "they said through gritted teeth"
    ]

    disgust_flairs = [
        "like the idea made their skin crawl", "as if the words were filth", "with a taste of bitterness",
        "like their patience had run dry", "like disgust clung to every syllable",
        "with a revulsion they couldn’t hide", "like they needed to wash the thought away",
        "with clear contempt", "like it physically hurt to say", "with a note of moral disgust",
        "like the world offended them", "with complete disdain", "as if they needed to spit it out",
        "like their pride was insulted", "with something rotten behind each word",
        "like their mouth tasted metal", "with a dry, cold edge", "like venom coated the sentence",
        "with bitter recoil", "like it was too repulsive to describe",
        "as if the thought came with a smell", "with no tolerance left",
        "as though it left a stain to say it", "with repulsion still rising",
        "like their words tried to reject the idea", "with vocal recoil",
        "like their morals had been stepped on", "like their body rejected the truth",
        "with eyes that screamed ‘ew’", "like the thought felt dirty",
        "with verbal acid", "like even silence was cleaner",
        "as if their very soul cringed", "with distaste in their breath",
        "like the words reeked", "as if reality was too disgusting",
        "with pure judgment", "with facial revulsion",
        "like everything about it was wrong", "with an inner shiver",
        "like it left a mark just to say it", "with narrowed, judging eyes",
        "with a shaking head of disbelief", "like the air got heavier with the thought",
        "with a sigh soaked in contempt", "like they needed to throw the thought away",
        "as if disgust made the words brittle", "with uncomfortable tension",
        "like their whole body recoiled", "as if the words came with a curse"
    ]
    opener = random.choice(disgust_openers)
    verb = random.choice(disgust_verbs)
    flair = random.choice(disgust_flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'


def generate_neutral_sentence(text: str) -> str:
    neutral_openers = [
        "Plainly,", "Just stating it,", "In a matter-of-fact tone,", "Without any rush,",
        "In a flat voice,", "With even tone,", "In a calm manner,", "Simply put,",
        "As if reading a note,", "With a neutral look,", "In an ordinary voice,",
        "As though it was routine,", "With no real emphasis,", "Unmoved,", "With casual delivery,",
        "Without blinking,", "Calmly,", "Steadily,", "Unfazed,", "As if reporting the weather,",
        "In a grounded tone,", "With no visible reaction,", "Even-tempered,", "Without judgment,",
        "Just as it is,", "As if it were fact,", "Flat and simple,", "With quiet tone,",
        "With no frills,", "Without decoration,", "No emotion in sight,",
        "Like stating a schedule,", "Without leaning into it,", "No drama attached,",
        "Soft-spoken and centered,", "Like it was routine,", "Nothing more, nothing less,",
        "With clarity but no spark,", "In a default tone,", "Without inflection,",
        "Balanced and basic,", "Straight to the point,", "Dryly,", "Level-headed,",
        "With a sense of control,", "Like it didn’t matter much,", "Toned down,",
        "Emotion withheld,", "Barely reactive,", "Composed and clean,"
    ]
    neutral_verbs = [
        "they said", "they noted", "they stated", "they mentioned", "they observed",
        "they added", "they spoke", "they replied", "they remarked", "they shared"
    ]
    neutral_flairs = [
        "as if it was just another fact", "with no feeling attached", "without adding much to it",
        "like it was background noise", "with a voice that didn’t lean in",
        "like it didn’t weigh much", "just as one might read a headline",
        "as if it had no deeper meaning", "with simple intent", "in a tone that didn’t sway",
        "as though the moment was passing", "like describing the weather",
        "without a second thought", "with plain delivery", "with no edge or warmth",
        "with just enough breath", "in a passing tone", "like brushing over a detail",
        "with nothing to prove", "like it belonged to nobody", "without making a statement",
        "like it was a placeholder", "in a neutral breath", "like it was data",
        "like a narrator in autopilot", "without marking it as important",
        "as if it didn’t need reaction", "in a quiet, centered way", "without layering it",
        "like reading from a list", "just moving through it", "in clean delivery",
        "like it wasn’t theirs to own", "bare and direct", "without color",
        "like a sentence in a manual", "in a filtered tone", "like it belonged to no mood",
        "without seeking response", "no more, no less", "like turning a page",
        "with little to hold onto", "in a barely-there tone", "like a pause that spoke instead",
        "without tilting the balance", "like ticking a box", "with no emotional weather",
        "like they were reading time", "like it slipped through unnoticed"
    ]
    opener = random.choice(neutral_openers)
    verb = random.choice(neutral_verbs)
    flair = random.choice(neutral_flairs)
    return f'{opener} {verb}, "{text}" — {flair}.'

def speak_it(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def generate_sentence(emotion, text):
    if emotion == "happy":
        return generate_happy_phrase(text)
    elif emotion == "sad":
        return generate_sad_sentence(text)
    elif emotion == "anger":
        return generate_angry_sentence(text)
    elif emotion == "fear":
        return generate_fear_sentence(text)
    elif emotion == "surprise":
        return generate_surprise_sentence(text)
    elif emotion == "disgust":
        return generate_disgust_sentence(text)
    else:
        return generate_neutral_sentence(text)


