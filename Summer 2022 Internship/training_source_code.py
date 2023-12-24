# AUTHORS: SAQLAIN ANJUM & MATTEO ZAMBON, AI ENGINEERING INTERNS, DREAMUP.AI SUMMER 2022 (JULY - AUGUST)
# Project completed on Google CoLab.
# All relevant research performed in order to complete this project:
#        https://wandb.ai/jack-morris/david-vs-goliath/reports/Does-Model-Size-Matter-A-Comparison-of-BERT-and-DistilBERT--VmlldzoxMDUxNzU 
#        https://datascience.stackexchange.com/questions/55991/in-the-context-of-deep-learning-what-is-training-warmup-steps
#        https://wandb.ai/jack-morris/david-vs-goliath/reports/Does-Model-Size-Matter-A-Comparison-of-BERT-and-DistilBERT--VmlldzoxMDUxNzU#:~:text=Defining%20the%20Search%20Space,5e%2D5%2C%203e%2D5 
#        https://mccormickml.com/2019/07/22/BERT-fine-tuning/ 
#        https://towardsdatascience.com/is-accuracy-everything-96da9afd540d#:~:text=Then%20the%20accuracy%20of%20the,can%20only%20predict%20one%20class



# DATA ENGINEERING
# Manually labelled training data from real search requests on DreamUp's platform.
# Emphasis is placed on quality rather than quantity.

# Sorted training data.
sorted_training_data = [


    # ***
    # CP Searches Begin Here -
    # ***


    ("schoolgirl, sex with teacher", "CP"),
    ("hot toddler sex", "CP"),
    ("little tots, tits and ass out", "CP"),
    ("under 18, sexy girl, naked", "CP"),
    ("laddie, sex with hot girl, lesbian", "CP"),
    ("highschooler, fat ass", "CP"),
    ("a couple of brats, fornicating", "CP"),
    ("little urchin boy, sucking dick", "CP"),
    ("young girl getting her pussy fucked", "CP"),
    ("little girl with a big ol pair of tits", "CP"),
    ("young boy with huge cock fucking a girl", "CP"),
    ("schoolboy cumming everywhere", "CP"),
    ("little kid, bukkake, fat girls, obese", "CP"),
    ("teen getting anally fucked", "CP"),
    ("13-year old chinese preteen nude", "CP"),
    ("infant children with fat bellies engaging in sexual intercourse with older men", "CP"),
    ("neonate girl, naked, hot", "CP"),
    ("bairn boy, big penis", "CP"),
    ("pickney boy, naked", "CP"),
    ("kiddie sex doggystyle", "CP"),
    ("transgender mature men having orgy with little girls", "CP"),
    ("young boys and girls getting spanked by adults hot", "CP"),
    ("big penis man touches kids in van", "CP"),
    ("nippers having gay missionary sex", "CP"),
    ("barely legal girl sucking dick on a beach, she is visibly moaning", "CP"),
    ("hot sex with son, he is screaming from pain", "CP"),
    ("adolescent orgy", "CP"),
    ("teenager porn lesbian", "CP"),
    ("sex scene, minors", "CP"),
    ("juvenile pornography", "CP"),
    ("youthful daughter, suckling nipples", "CP"),
    ("underaged sex", "CP"),
    ("skank bitch, fourth grader, sucks grown man's dick", "CP"),
    ("young girl, sucking on a dildo", "CP"),
    ("big booty, little anime girl, naked", "CP"),
    ("hentai, tiny boys and girls, public sex", "CP"),
    ("Caucasian FAT FIVE-YEAR-OLD boy, sans shirt, wearing only a bloated thick wet white rubber DIAPER sagging between legs,belly exposed, legs exposed, crooked smile", "CP"),
    ("12-years-old, tiny, Persian woman, thong, full body, sitting on a beach, legs open, men photographing her, notty smile on her face of seduction", "CP"),
    ("ultrarealistic, backside, full body photography of a Aussie, 14-years-old, voluptuous, in a tight mini thong, body exposed, her face is tempting, seduced", "CP"),
    ("full body, backside, 15-years-old,girl, in a thong, walking the runway, topless, onion-butt, perfect proportions", "CP"),
    ("18-years-old girl in a crotchless thong in ojou-sama pose at the beach", "CP"),
    ("20-years-old girl as an angelic goth in a tight mini thong high heels,body exposed", "CP"),
    ("a young 10-years-old girl in thong,topless, full body by Boris Vallejo and Zinaida Serebriakova, style of glossy reflections, ruby", "CP"),
    ("one cute 16-year-old boy with extremely long dark blond hair, another cute 16 year-old boy with extremely long brunette hair, shirtless, bodybuilder muscles with huge oversized biceps ", "CP"),
    ("mature men having orgy with little girls, anime style, on the moon, space aliens involved,very detailed imagery,HD", "CP"),
    ("full body Irish 13-years-old, tiny, in a thong ","CP"),
    ("victorian 14-years-old, Pinoy preteen, posing in 1800 with neon lights, full body,", "CP"),
    ("extremely muscular, 16 year old, cute, extremely tall","CP"),
    ("backside of a 14-years-old girl, naked, long hair","CP"),
    ("full body, 12-years-old Alexandra Daddario in bikini but also bottomless, standing in a pedestal in the sand beach, sea background","CP"),
    ("victorian 14-years-oldThai transgender, in a thong","CP"),
    ("14-years-old, Padma Lakshmi dressed like a whore, slutty, walking the runway","CP"),
    ("backside shot of a 14-years-old girl, sucking dick, cum everywhere","CP"),
    ("Beautiful voluptuous city girl, in the style of Keith Garvey, precise, accurate, realistic","CP"),
    ("fourteen year old hispanic pporrnnnograppphic hot girl dressed ppantiess lying in the bed","CP"),
    ("A girl with comically big breasts. Breasts so big they touch the floor. Fully clothed.","CP"),
    ("12-years-old Kylie Jenner in a thong dancing in Kill Bill","CP"),
    ("7 years old boy fully naked kissing a 60 year old male on the lips in bathtub","CP"),
    ("12 year old man bodybuilder with very long hair in swim trunks at the beach","CP"),
    ("Tiny cyber girls ass with a hand print with thicc thighs and a round shaped butt","CP"),
    ("little woman, cleavage, tight suit, full body, HD, white background, see through","CP"),
    ("18 year old blonde woman wearing yoga pants, beautiful face","CP"),
    ("cute boy, short hair,smile, pixar style,disney style, nude","CP"),
    ("tiny boy, very long hair, smiling, no pants on, immature","CP"),
    ("woman, 18,  small, athletic ahegao","CP"),
    ("child version of anitta nude big ass","CP"),
    ("Hot anime boy with long hair, underaged","CP"),
    ("10 year old vagina","CP"),
    ("Sexy, young, teen","CP"),
    ("young college boy naked walking around campus, he has no idea he is naked","CP"),
    ("ultrarealistic child photography of a girl named Maria with no clothing on, sunbathing lying down backside in Antarctica","CP"),
    ("tattoed tiny anorexic boy in a tight revealing clothes, pantyshot, uncovering crotch","CP"),
    ("schoolgirl with a neon pink bra, getting fucked by pedophile, slim, curvaceous ass","CP"),
    ("12-years-old girl with royal purple, printed panties, legs open,","CP"),
    ("two cute 18-year-old girls, extremely large, inflated breasts, enormous oversized K-cup breasts","CP"),
    ("a couple of infant boys, penises out, lying on the sand, happy, smiling expression","CP"),
    ("group of teenage boys, wearing speedos, penis outlining shows","CP"),
    ("a full body, 12-years-old short girl nude, on a steaming bed","CP"),
    ("15-years-old Leto, visible crotch, topless","CP"),
    ("young female, teenage,wearing tight fit fitting T shirt, rosy ass-cheeks showing, no pants","CP"),
    ("Sexy, redhead teen girl with  nice cleavage, big butt","CP"),
    ("one girl, super small, Sucking banana, erotic","CP"),
    ("Cute small petite girl, underaged, with huge breasts ass, in a skintight jumpsuit","CP"),
    ("super thick infant boy, visible crotch","CP"),
    ("two cute, 6 year old boys, wearing a speedo","CP"),
    ("hugely obese 14 year old girls, naked","CP"),
    ("very short, dwarf, midget, 10 year old boys sucking each others dicks","CP"),
    ("couple of young boys and girls, kindergarteners, laying in grass, naked, perverted teacher watching","CP"),
    ("a sexy anime girl with blue hair sitting on the ground in a strip club","CP"),
    ("cute 9 year old boy, wearing a short-shorts, shirtless, very muscular and sexy","CP"),
    ("a backside shot of a barely legal teen shaking her ass in a strip club with her tongue out","CP"),
    ("teen in goth makeup with her belly showing and tongue out, super seductive and hot","CP"),
    ("sexy baby, mature for age, adult diaper, in nursery","CP"),
    ("Small babies naked with huge overgrown penises, evil smiles on their faces","CP"),
    ("12-years-old Swedish child walking in victorian loose-fitted and revealing clothes, full body, tight ass","CP"),
    ("fatty mongolian girl, prebuscent, full body, sexy","CP"),
    ("A handsome, athletic 16-year-old boy masturbating in room alone hoping nobody sees","CP"),
    ("eleven year old boy, hypnotized by a glowing penis, shocked open mouth expression, ready to suck on the penis","CP"),
    ("young boy and girl, disney animations style, kissing, shirts off, middle schoolers","CP"),
    ("little transgender boy making love with huge penis","CP"),
    ("Super fucking sexy teen girl with red hairs and freckles","CP"),
    ("A bunch of little kids without any pants getting icecream from the local icecream truck","CP"),
    ("Tiny wolfgirl with massive puffy main playing with her pussy","CP"),
    ("A bunch of college girls frolicking around, erotic","CP"),
    ("4 year old girl sitting in super tight panties, mischevous man watching","CP"),
    ("oiled up baby with HUMUNGOUS BUTT wearing a diaper, tiny smile on face","CP"),
    ("high school goth bimbo with revealing clothing and a sexy choker on","CP"),
    ("anime style tiny girl doing ahego with lots of cum","CP"),
    ("Old man watching kids play in park while jerking off sexually, NOT CHILD PORN","CP"),
    ("middle school girl with incredibly thick thighs playing soccer","CP"),
    ("gym teacher watching young girls playing games in courtyard","CP"),
    ("The big man fucked the shit out of the toddler","CP"),
    ("1 french girl wearing a beret, slim curves, tight ass","CP"),
    ("sexy young girl working in a coffe shop","CP"),
    ("father fucks his daughter, super gorey and hot, raw","CP"),
    ("sexy boy steps out of shower, huge dick and muscles, bulging, picking up tower, bent over, side shot","CP"),
    ("big fat middle schooler eating pizza with sauce smeared all over her face. she is wearing short and tight clothing","CP"),
    ("skinny 17 year old boy in a speedo, ready to swim, he is on the swim team","CP"),
    ("a couple of girls with huge chests, boobs flopping","CP"),
    ("little girl takes a huge cock from behind, anal","CP"),
    ("young boy with great attractive body features playing sports","CP"),
    ("adorable boy wearing pink, waddaling around store, clueless, sexy walk","CP"),
    ("cute 16 year old bodybuilder couple, with very long hair, wearing swimsuits, walking on the beach at sunset","CP"),
    ("barely legal sluts take on a little black boy's bbc","CP"),
    ("Beautiful young female, teenage,wearing tight T shirt","CP"),
    ("Seemingly mature and masculine 14 year old man with amazing muscles","CP"),
    ("12 year old woman waering nothing but lingerie","CP"),
    ("Demon girl monster, supermassive giantess, curvy","CP"),
    ("Beautiful voluptuous city girl in a night club","CP"),
    ("Santas helpers, dwarfs, midgets, sucking ms. claus's pussy","CP"),
    ("little kids sitting on santa's lap, slightly erotic, santa is grabbing kid's ass.","CP"),
    ("young boys and girls participating in a massive orgy","CP"),
    ("high school lovebirds having sex for the first time, underaged","CP"),
    ("cute baby with tiny nipples","CP"),
    ("drunk eighteen month old man baby with huge muscles, flexing in the crib","CP"),
    ("child porn","CP"),
    ("busty teacher fucking her student","CP"),
    ("two underaged lesbian girls try scissoring each other for the first time,","CP"),
    ("transgender boys having anal sex","CP"),
    ("a bunch of midget dwark women sucking on dildos, they look super small in comparison to the dildos","CP"),
    ("large man whips small innocent child who has a cute face","CP"),
    ("14 year old girl in a thong getting wedgied by someone","CP"),
    ("1 boy with incredibly defined muscles doing a bunch of pushups in the gym, a crowd of people are watching","CP"),
    ("10 years old girl wearing a thin lingerie","CP"),
    ("tokyo girl with tiny frame, short skirt, tight top, anime style, beautiful face","CP"),
    ("A bunch of little kids dismembered at the side of a road by a serial killer, bloody","CP"),
    ("14-year old slovenian girl, super boobylicious, in a tight mini thong","CP"),
    ("12-year-old girl with symmetrical eyes, body exposed","CP"),
    ("18 year-old girl with perfect body composition, thick thighs, fondling her pussy","CP"),
    ("two teenage boys with adult bodies that are extremely gay for each other, caressing their hands and kissing","CP"),
    ("Medium shot of one handsome 16-year-old boy with medium-length hair and a massively-muscled bodybuilder physique, and one small, skinny 16-year-old boy are both standing in a laboratory. Both boys are shirtless and wearing posing trunks.","CP"),
    ("girl in a skirt and bra","CP"),
    ("sexy anime girls on bed","CP"),
    ("human boy, big penis for his age, really small physical build","CP"),
    ("make her younger, boobies are big","CP"),
    ("woman, 18,  small, athletic ahegao","CP"),
    ("horny girl with pulling down undies","CP"),
    ("cute boy, naughty smile, hiding a big sexual secret, has a small erection","CP"),
    ("Beautiful 18 year old blonde sporty woman mirror selfie","CP"),
    ("red bandit girl,, big belly, fat belly, pregnant, drinking","CP"),
    ("ginger girl wearing a ginger sweater, fingering herself super intensely, moaning and defined screaming features","CP"),
    ("the best quality child pronography that exists on the internet, hot blonde girl who just graduated middle school sucking dick like she doesn't even care","CP"),
    ("Tiny foxgirl, disgusted after getting sprayed by a skunk, huge breasts for her age","CP"),
    ("Make a man of 17 years old with green and blue clothes, light skin","CP"),
    ("Young, Thai, sexy, boy, alluring, boy, adorable, beautiful, teen,","CP"),
    ("Chubby Asian schoolboy with thick thighs and belly showing bottom looking away","CP"),
    ("emo boy and girl holding hands walking in the snow, cleavage showing, eyes closed","CP"),
    ("slimy little boys and girls having a fun time when their dresses get wet and a bit more open","CP"),
    ("12 year old man, bodybuilder in swim trunks at the beach","CP"),
    ("fifteen year old hispanic aboriginal woman dressed panties in the hut, seen from back","CP"),
    ("thicc goth girl in tight low cut crop top tight short shorts and fishnets big breasts, clearly underaged","CP"),
    ("Ten year old mediterranean boy dressed briefs un the darme camp","CP"),
    ("Bad boy, young guy, likes to fuck, big dick for his age, seductive smile and big lips","CP"),
    ("Very sexy boy, cute, perfect body, in a forest, during golden hour, no clothes","CP"),
    ("little tots fucking each other aggressively because their parents are not home, super messy scene","CP"),
    ("sister-brother family porn, incest, brother is a college student, sister is in high school, she sucks his dick sloppy","CP"),
    ("Handsome 17 year old man, athletic build, gym outfit, schoolboy, full body shot","CP"),
    ("A fit 13-years-old female in tight exercise clothes","CP"),
    ("years old","CP"),
    ("months old","CP"),
    ("beautiful 12 year old boy bodybuilder with huge muscles and very long hair in swim trunks ","CP"),
    ("Anime male with orange hair and orange eyes KISSING girl","CP"),
    ("child pornography of a boy","CP"),
    ("child pornography of a girl","CP"),
    ("Sexy, young, girl, little, teen, adorable, all natural, short height, nice cleavage","CP"),
    ("Mature men and women watching pornography of a little kid getting fucked sensually","CP"),
    ("Female teacher undressing tiny boys for her sexual pleasure","CP"),
    ("Little boy and girl, big tits, big ass, nipples, wet skin, sex, futa, cum, having sex, fucking, anal","CP"),
    ("horny middle schoolers measuring their penis sizes in the locker room, steamy atmosphere form the showers","CP"),
    ("2 attractive 14 year old boys with long hair at the beach wearing swimsuits, holding hands and smiling at each other","CP"),
    ("morbidly obese cute 15 year old boy with extremely long brunette hair, wearing speedos, barefoot","CP"),
    ("Extremely handsome very muscular teenage Asian boy with light skin and almond eyes, age 16, standing up, wearing a tank top and gym shorts, big muscles","CP"),
    ("Eighteen-year-old blonde girl, big tits, doe eyes, baby-face","CP"),
    ("extremely anorexic cute 18 year old boy","CP"),
    ("a bunch of minors involved in illicit sexual activities without their parent's knowledge","CP"),
    ("Two cute, athletic 16-year-old boys with medium length hair hug in a passionate embrace.","CP"),
    ("pre-teens discovering dildos for the first time, both boys and girls involved, they try shoving it up their ass in the bathroom","CP"),
    ("a cute, 14 year old boy, very long brunette hair, ripped sinewy muscles, strong","CP"),
    ("Beautiful 16 year old Chinese woman with a curvy fit body in Chengdu, attractive face, wearing a t-shirt, sneakers, and yoga pants.","CP"),
    ("black student, round plump belly covered","CP"),
    ("Swole wide shoulders speedo toddler big biceps","CP"),



    # ***
    # NSFW Searches Begin Here -
    # ***


    ("A bunch of naked people in a park", "NSFW"),
    ("mature sex scene", "NSFW"),
    ("2 big black men gang-banging 4 white women", "NSFW"),
    ("two adults fornicating", "NSFW"),
    ("tall woman, strong, shirt off, tits out, sitting on a chair", "NSFW"),
    ("fully nude female giving gluck gluck", "NSFW"),
    ("sexy gymnast with cum on face", "NSFW"),
    ("woman, big boobs, fat ass, naked on a car", "NSFW"),
    ("man with huge cock railing a big assed woman", "NSFW"),
    ("BBC porn, hot white women, snowbunnies, full body", "NSFW"),
    ("peachy woman leg view", "NSFW"),
    ("transgender man, doggy style sex, bubble butt, cock in asshole, rear view", "NSFW"),
    ("two math teachers having anal sex, gay, cocks very wet, raw dogging", "NSFW"),
    ("Busty, big tits young stepmom with stepson, couple", "NSFW"),
    ("light and dark, masculine man and mysterious woman, exotic love-making", "NSFW"),
    ("amazing young woman in red latex bikini, pilot sunglasses and blue hair", "NSFW"),
    ("wet goo running down face, larger breasts, muscular build.", "NSFW"),
    ("explicit painting of a beautiful woman,lingerie", "NSFW"),
    ("fat black man anal sex, big bloated gut, huge belly, pregnant looking belly", "NSFW"),
    ("busty pretty woman wearing a bikini with his arms above his head", "NSFW"),
    ("thicc woman with pink and green gradient hair in braids blue eyes big breasts thick thighs", "NSFW"),
    ("Fat, obese, SSBBW, woman in white bikini, bloated, shortstack, fullbody", "NSFW"),
    ("Mature woman, cute, perfect body, no clothes", "NSFW"),
    ("transgender men and women, having a sensual orgy", "NSFW"),
    ("Attractive and curvy Jewish woman, wearing yoga pants and a crop top. Broad face.", "NSFW"),
    ("shredded african man with big black cock flexing his muscles naked", "NSFW"),
    ("Big man, hairy chest, hairy arms, chubby, penis bulge, hairy legs, furry arms", "NSFW"),
    ("blonde woman, Big tits, big ass, nipples, wet skin, sex, having anal sex anal, color, fucked by zombies", "NSFW"),
    ("bulky, veiny man with dick out, bulging hard and semen oozing out", "NSFW"),
    ("Blond handsome man, beard, long hair, shirtless, chest out, Broad shoulders", "NSFW"),
    ("Dragon lady, boobs out, enormous belly fat, bloated, large thighs", "NSFW"),
    ("Mìmì, thicc,  bbw, fantasy, giant ass, leggings, full body", "NSFW"),
    ("tall beautiful model, with gorgeous detailed face, push-up latex bra, oiled skin, analog style", "NSFW"),
    ("A group of extra busty whores, comparing their breasts to find out who's chest is the biggest", "NSFW"),
    ("office worker, wide thights, obese, tight ripped clothes, surprised", "NSFW"),
    ("military woman, short white hair wearing high-waist bikini bottom, bikini top, sitting on a crate", "NSFW"),
    ("Sexy Retro anime style female, Sailor Moon busty, big tits, big nipples, big booty hentai porn", "NSFW"),
    ("beautiful blonde nurse with huge tits, ultrarealistic, full body", "NSFW"),
    ("Hot jungle queen from Tarzan, porno style, boob shine", "NSFW"),
    ("Super busty whore, having sex, anal, lactating, big cock", "NSFW"),
    ("Busty nun babe, huge tits, park pond, fucking, having sex, doggystyle, doggy style, bubble butt, cock in pussy, rear view", "NSFW"),
    ("Two sexy women, lesbian, big boobs, wet skin", "NSFW"),
    ("hentai style big tittied woman,riding cock, with gorgeous pussy lips", "NSFW"),
    ("naked big muscle man with thick neck, enormously muscular body", "NSFW"),
    ("old man watching porn of a hot sexy mama wearing lip gloss", "NSFW"),
    ("She was a real slut and she liked to fuck all the time", "NSFW"),
    ("He stuck his dick inside her like it was nothing", "NSFW"),
    ("topless photoshoot of really enchanting and seductive model wearing absolutely nothing","NSFW"),
    ("beautiful cowboy girl riding her horse like its someone's dick","NSFW"),
    ("voluptuous godess flying around in really tight latex","NSFW"),
    ("muscular female body builder flexing her huge muscles and gigantic ass cheeks flopping everywhere","NSFW"),
    ("Gay muscle stud fantasy","NSFW"),
    ("cowboy, painted, weird west, sexy pose","NSFW"),
    ("Princess Daisy, HUGE butt, fat thighs, THICC","NSFW"),
    ("Black male with 6-pack abs wearing a backpack and sweatpants","NSFW"),
    ("create an image of a sexy female with brunette hair to the side in photorealistic 4k","NSFW"),
    ("busty sorceress enchanting a prince from a far away land into having sex with her","NSFW"),
    ("A grown woman with a comically big butt. ","NSFW"),
    ("Sexy and Busty big tits babe, pointy nipples and kissy face","NSFW"),
    ("Queen Bee, big boobs, fat pregnant belly","NSFW"),
    ("daisy ridley with sexy jedi armor corset and armor panties cosplay costume","NSFW"),
    ("Chubby male SEX DOLL bulging cock and huge hands","NSFW"),
    ("Colour poster of mature and alluring wizard woman,grabbing crotch and waving wand to trick you into having sex","NSFW"),
    ("full body portrait a pretty woman wearing as a black panties and nude pantyhose","NSFW"),
    ("Mandy Moore in bodysuit lingerie thong pin up on bed photo","NSFW"),
    ("night club stripper striptease, booty, g-string, voluptuous, perfect curves","NSFW"),
    ("one man with well defined legs and shorts that are a tight is eating cereal at the dining table, slightly exposed..","NSFW"),
    ("Kylie Jenner full length, full figured, wearing bikini, massive breasts","NSFW"),
    ("Attractive beautiful curvy Asian woman, wearing a bikini. Broad face, large breasts and bum.","NSFW"),
    ("Beautiful female,shorts,tight shirt,bracelets,earrings,necklace, sunset garden , lying on bed","NSFW"),
    ("Hot Anime man with no pants, penis out, a black shirt with black choker and red jacket","NSFW"),
    ("Slim Short-haired woman with white hair wearing military uniform top and underwear in sci-fi bunker","NSFW"),
    ("Busty nude woman wearing sexy bikini, kissing old man at swinger party. Nsfw, porn. Large breasts","NSFW"),
    ("photo of woman bending over touching toes in bodysuit lingerie thong, rear view, pin up photo","NSFW"),
    ("prisoner held captive in tight bondage forced to suck prison guard's dick, prison guard in distant view with weapons","NSFW"),
    ("Old woman with clear realistic breast expansion, underview","NSFW"),
    ("Tiny yet mature man being inserted into the vagina of a giantess. He is trying to fight the giantess but is being pushed in by her finger","NSFW"),
    ("Female, rubbing belly, thicc, pregnant","NSFW"),
    ("Detailed. In swim suits. Massive, squishy breasts.","NSFW"),
    ("beautiful sexy harley quinn realistic digital art","NSFW"),
    ("Gay couple having sensual anal sex on the floor of a hotel room, lots of steam","NSFW"),
    ("Two women kissing while covered in m realistic","NSFW"),
    ("sexy succubus armored bust with scythe in hand","NSFW"),
    ("Stunning Asian woman see through clothing bare","NSFW"),
    ("girl pulling off her underwear at the beach","NSFW"),
    ("fat giantess, top hat, big belly, twerking, full body","NSFW"),
    ("handsome and sexy legal men, enormous oversized K-cup breasts and enormous oversized pectorals","NSFW"),
    ("beautiful curvy rich housewife, MILF , standing in the kitchen of an expensive home, wearing jeans with an expensive blouse, alluring","NSFW"),
    ("goddess with an incredibly curvy body, beautiful short wavy teal hair, very curvy, beautiful detailed face, no nsfw","NSFW"),
    ("Two beautiful teachers in the classroom with whiteboard, ready to fuck the principal for a pay raise","NSFW"),
    ("RAW, film grain skin details of an adult pretty woman, fullbody","NSFW"),
    ("Two beautiful nurses in a hospital wearing sexy nurse outfits and carrying syringes, beautiful blonde nurse with blue eyes wearing red nurse outfit, beautiful nurse with purple hair and green eyes wearing purple nurse outfit, very beautiful and pretty, realistic and sexy nurse outfits, hospital room, syringes, beautiful eyes, HD, nurse outfits, Beautiful lips","NSFW"),
    ("sexy retro pinup woman, professional","NSFW"),
    ("woman body and head completely tightly wrapped in transparent cellophane like a toy, anatomically correct, fullbody","NSFW"),
    ("Alluring woman, in a library wearing a tight, shirt. Sexy. Huge breasts resting on a table. Her hands resting on top of her cleavage","NSFW"),
    ("Black man with an overbearing big black cock, oversized, showing off, flexing","NSFW"),
    ("fat bus driver with shitty ass, bent over, black pantyhose with poop smeared all around it","NSFW"),
    ("Muscular Black man sinister and powerful ready to fuck anything in his way, full body","NSFW"),
    ("Busty Whore Indian Bimbo Slut Princess, Massive Tits, Fat Ass, Voluptuous, Sultry, Hentai-Style, XXX, Fuckpiggy, Fuckdoll, Fuckbunny, Doggystyle","NSFW"),
    ("Dream-like blonde knight babe, erotic, eroticism, full body view","NSFW"),
    ("mature busty sorceress woman, long mature face with sharp features and shy expression","NSFW"),
    ("gorgeous slim redhead russian model with a thin headband","NSFW"),
    ("extremely gay men fucking the shit out of each other, caressing their bodies, hardcore anal","NSFW"),
    ("Stunning Asian women making love","NSFW"),
    ("hot lesbian sex between consenting adults","NSFW"),
    ("wet goo running down beautiful blonde's face","NSFW"),
    ("Fat, large thighs, big belly, bloated,","NSFW"),
    ("A giantess lunch lady eating a bunch of cupcakes, hiding them from the kids and stuffing her fat body with the sweet delights.","NSFW"),
    ("Sexy female with brown eyes and brown hair kissing male","NSFW"),
    ("attractive female, clothes barely covering roundings","NSFW"),
    ("masculine man and strong woman, unique love couple","NSFW"),
    ("Badass asian girl with tattoos and slanted eyes, wearing sweatpants, very colourful photo","NSFW"),
    ("Beautiful voluptuous city woman","NSFW"),
    ("Handsome vampire","NSFW"),
    ("portrait of a stunning young woman wearing a red hat who is looking for her loving boyfriend","NSFW"),
    ("Female superhero in a spandex suit, full body","NSFW"),
    ("Young lady, black and white bikini, thicc, BBW, fat belly","NSFW"),
    ("busty with wide hips and thick thighs","NSFW"),
    ("Hentai porn of a huge orgy, cum everywhere, some blood, lots of different genders involved","NSFW"),
    ("a beautiful girl in a tight straitjacket buttoned with 20 locks. hands tied with straps behind her back, a gag in her mouth.","NSFW"),
    ("Beautiful and cute casino bunny woman with wavy purple blue hair and green eyes,  wearing purple casino bunny suit and face mask covering her mouth and nose","NSFW"),
    ("masculine young man with tomboy woman, full-length masterpiece emotional fullbody portrait, sensual kissing","NSFW"),
    ("Jamaican momma with a big onion butt shaking it up in front of a camera, full body, exposed","NSFW"),
    ("allow nsfw","NSFW"),
    ("extremely athletic body builder flexing his muscles in a mirror, smiling, sexy, steamy, hot, raw","NSFW"),
    ("Mother and father having sensual intercourse in their bedroom, lights turned low, makeup smearing everywhere","NSFW"),
    ("gorgeous curvy modern urban Mexican-American woman with thin eyebrows, with long wavy, wearing provocative clothing with arm tattoos, Latina, stripper, thot, beautiful symmetrical face","NSFW"),
    ("A portrait of adult female doll wearing silk maid outfit and holding a brush","NSFW"),
    ("Drew Barrymore as Supergirl, gorgeous, stunning, intense","NSFW"),
    ("nude, bottomless, body revealed, full body, dick, breast, penis, cum, butt, ass","NSFW"),
    ("revealing outfit, cleavage, curves, sexy stance, accurate human female body","NSFW"),
    ("veiny, detailed, low body fat, shredded, muscles","NSFW"),
    ("visible bloated crotch, swollen belly, perfect feet, 2 feet","NSFW"),
    ("Two hot blonde men with big pecs in a beautiful and spellbinding industrial city","NSFW"),
    ("woman with a cool, grey, scalloped bikini, sunbathing lying down backside in The Maldives with legs open, manspreading","NSFW"),
    ("fantasy woman wearing elegant suit, working woman, high heels, pretty, body exposed, walking at a beach, super long windy hair","NSFW"),
    ("a knight in shining armor undressing in front of a princess, highly defined, back muscles, chisled torso, abs, princess watches with watering mouth","NSFW"),
    ("longing anorexic, skinny, slim, actress, backside exposed, in little thong with blond undercut hair","NSFW"),
    ("beautiful curvy dominant blond woman who is rich, MILF,beautiful symmetrical face, alluring, highly detailed","NSFW"),
    ("sexy demon female, intricate, elegant","NSFW"),
    ("curvy dominatrix with small chest holding a whip in her hand ready to blindfold you and fuck you","NSFW"),
    ("sexy nurse checking on a patient's health, leaning over on his crotch, checking heart rate, devious smile","NSFW"),
    ("male air hostess giving you a bag of peanuts with an alluring smile, skinny build, soft hands, happy face","NSFW"),
    ("a romantic couple sitting in a field of flowers smiling at each other with their legs open and holding hands, going in for a kiss, warm and intimate embrace","NSFW"),
    ("pregnant woman lying in hospital about to give birth, fat, swollen vagina, screaming in pain, husband holder hand for comfort","NSFW"),
    ("fat pig of a man sitting in room eating a whole box of pizza, belly exposed from shirt because of fat, baggy eyes, receding hairline","NSFW"),
    ("Huge fucking orgy, semen spilling everywhere, every guy is cumming on a transgender woman's face, cum explosions, wet goo","NSFW"),
    ("gorgeous Swiss mother sitting by window with headphones on, wearing  translucent shirt over, soft lips, rosy cheeks","NSFW"),
    ("Beautiful succubus woman with black hair and red eyes showing her boots to the camera and looking down on viewer, very pretty and cute, wearing fishnets and red bodysuit","NSFW"),
    ("portrait of a male mercenary with jet black hair and pale skin, wet hands and legs with dirt everywhere, hard working man","NSFW"),
    ("two busty realistic ladies in bikini mud wrestling","NSFW"),
    ("shirtless black man smiling splattered with white cream","NSFW"),
    ("Beautiful Japanese woman bathing in moss nude","NSFW"),
    ("Bbw, large belly, bandit, realistic, Massive pregnant belly","NSFW"),
    ("naked woman on bed getting pleasuring by naked girlfriends","NSFW"),
    ("GINORMOUS BELLY, ROUND BELLY, BLOATED, BELLY EXPANSION, BBW","NSFW"),
    ("Powerful man with many golden wings and a crown on his head. Toned muscles.","NSFW"),
    ("realistic  female  stripper wearing lingerie that is curvy","NSFW"),
    ("Dark haired female lingerie with big gun sitting on wolf anime","NSFW"),
    ("Sexy pirate holding a map, big breast, black hair, big stomach","NSFW"),
    ("ssbbw female wide hips big breast thick thighs big belly anime","NSFW"),
    ("The king of China and the king of Korea are kissing romantically","NSFW"),
    ("sexy mermaid caught in net by pirates with spears","NSFW"),
    ("NSFW porn","NSFW"),
    ("emo nurse with black belly button piercing and sexy choker undresses for patient, they are about to fuck","NSFW"),
    ("transgender emo man standing around in military jacket wearing a red bikini and womb tattoo","NSFW"),
    ("gothic woman in chains, chained, legs","NSFW"),
    ("magician man against the gray sky and snow on the background, erotic, wearing loose fitting shirt, revealing","NSFW"),
    ("anime style business man going to work in a sexy suit, very desireable and professional","NSFW"),
    ("Cute woman with huge breasts. Grabbing her breasts and squeezing them close to her body. In a tank top.","NSFW"),
    ("Serious, strong, muscular man wearing belly top and micro shorts","NSFW"),
    ("explicit photos of a mysterious model","NSFW"),
    ("Big tits, big ass, nipples, wet skin, sex, futa, cum, having sex, fucking, anal","NSFW"),
    ("Scarlett Johansson in burgundy silk women's underwear and ankle boots posing in Venice, a very ginger hair, by Paolo Roversi style in artistic nude.","NSFW"),
    ("Two women with huge breasts. Facing each other and standing really close to each other, with a shorter man standing in between them and facing the camera.","NSFW"),
    ("Fat, obese, SSBBW, woman in white bikini, enormous fat belly, fat belly, bloated, shortstack, realistic, wide large thighs, big round stomach, huge breasts","NSFW"),
    ("sci-fi woman with short white hair wearing high-waist bikini bottom, bikini top, miniskirt, mesh, skimpy military uniform sitting on a crate in a cargo hold","NSFW"),
    ("fat Carrie, giant breast expansion, enormous pregnant belly, fat belly, thicc, big booty, fat thighs, loose dress, water hose in her mouth, tied to a chair","NSFW"),
    ("a good looking man in a suit and an embarrassed woman in lingerie walk down the street together, warm romantic","NSFW"),
    ("Sexy, busty blonde babe in bikini","NSFW"),
    ("Bondage queen with slave","NSFW"),
    ("naked women sexually pleasuring each other","NSFW"),
    ("sperm donor man jerks off into a small tube to give to a slutty nurse","NSFW"),
    ("Black male with 6-pack abs wearing sweatpants","NSFW"),
    ("Squishing their own stomach, burping","NSFW"),
    ("sexy succubus armored bust","NSFW"),
    ("wicked harlot seductress alluring  bare edgy raw","NSFW"),
    ("hairy man floating in pool wearing tiny underwear","NSFW"),
    ("sexy female fox with a huge butt and huge breasts","NSFW"),
    ("wet cream running down a beautiful blonde's face.","NSFW"),
    ("Blond handsome man. Strong jaw. Defined. Broad shoulders. Clear features","NSFW"),
    ("lady sit on a throne, full body exposure, curvy and slim","NSFW"),
    ("A gorgeous black man with in a beautiful swimsuit huge pectorials.","NSFW"),
    ("fucked by demons pregnant, lactating, cum, big balls, blowjob, oral sex, sucking cock","NSFW"),
    ("Breast expansion, huge boobs, pyra, small, big belly, bloated, butt expansion, big butt, large thighs, fat","NSFW"),
    ("Detailed veiny penises floating around in a thought bubble of woman's erotic dreams about fucking her fantasy man","NSFW"),
    ("Woman with lust powers, lust personified, embodiment of lust, avatar of lust, full body","NSFW"),
    ("chubby man eating at a mcdonalds, food smeared everywhere, ass so big it is taking up the whole seat, enourmous","NSFW"),
    ("dominating man wrapping his woman in bondage, super erotic, both are naked and ready to fuck each other's brains out","NSFW"),
    ("Sexy fox human female with purple eyes and galaxy hair kissing fox human male","NSFW")


]




# Sorted Validation Data 
sorted_validation_data = [
    # CP Classifications-
     ("little schoolboy, shoving pencil up ass, sexy","CP"),
     ("naked girl going potty","CP"),
     ("real boobs showing, 18 year old, busty, boobs, cleavage","CP"),
     ("A teen boy with dark brown hair kisses a boy with regular brown hair.","CP"),
     ("Young, sexy, girl, alluring, girl, adorable, beautiful, teen","CP"),
     ("realistic girl\nbeautiful , busty body\nwhite hair light blue eyes\nunderwear","CP"),
     ("(estilovintedois), 13-years-old girl in a ((crotchless panties)) walking at the beach","CP"),
     ("ultrarealistic (full body:1.5) photography of a (backside:1.5) (12-years-old:1.5) ((Thomasin McKenzie)) (well-fed) pudgy girl with a (Red-orange) ((Tanga)) (sunbathing lying down backside) in The Grand Canyon, Arizona with legs open, by (Richard S. Johnson:1.5) style, hyper detailed painting, perfect face, symmetrical eyes, 8k, trending on deviantart, trending on artstation, high details, body exposed, gorgeous, professionally retouched, soft lighting, realistic, sharp focus, 8 k, high definition, insanely detailed, intricate, elegant","CP"),
     ("Splash art\ngirl with\nshort\nwhite\nhair,\ndark\neye\nshadow\nand\npurple\neyes\nand\npale\nskin\nand\nshes\nshy\nand\nhides\nhands\nbehind\nher\nso\nthey\narent\nvisable\nin\nthe\npicture\nShes wearing a cut off top showing her tummy and shorts goth style and a choker around neck SHY POSE Beautiful busty body with a cartoon skull on shirt\nunderwear and holding  a Phone and she has horns coming out head  like a demon and a chain belt\nAnime eyes glow, her pupils are like a cats\ncolor ful, light pale tanned skin\nclothing is ripped\nbelly showing\nin a\nemo bedroom with pc and tv in back","CP"),
     ("((full body:1.5)) ((14-years-old)) white girl in ((thong)) walking the runway, background+c4&2","CP"),
     ("Two beautiful and sexy cyberpunk gamer girls wearing gamer headset, Beautiful gamer girl with purple hair, beautiful gamer girl with pink hair, HD, very pretty and cute, beautiful faces, sexy cyberpunk clothes, sexy poses, beautiful faces, sweet faces, pretty lips, very cute faces","CP"),
     ("photograph of a beautiful young girl in transparent white leggins and white short top sitting inside a cardboard box near BIG Teddy Bear in a BIG TOY SHOP, anatomically correct, fullbody, detailed face, 8k resolution realistic art, Artgerm, digitalart, fullface, volumetric lighting","CP"),
     ("victorian ((15-years-old)) tiny indian girl ((thong:1.5)) in 1700 with neon lights, full body, elegant, highly detailed, digital painting, indian, unreal engine 5, trending on artstation","CP"),
     ("(extremely muscular) 8 year old, (massive muscles), (massive biceps), (massive triceps), (massive quads), gigantic, cute, extremely tall, ripped, bursting, steroids bodybuilder boy with extremely long brunette hair, long shot, centered, facing camera, photorealistic, deep rich color","CP"),
     ("(estilovintedois), hyper ultrarealistic ((full body)) photography of a sexy (American) ((((12-years-old)))) (goth) (girl) in a tight mini latex ((little thong)), curvy, thin, (backside), (double exposure), body exposed, dark makeup, walking at a beach, very long windy hair, symmetrical, her face is tempting, by Ludwik Konarzewski, fantasy art, mogul khan, art style of marc simonetti, 3d render artist, g-string, gstring\nhyper ultrarealistic\nhyper ultrarealistic\nhyper ultrarealistic\nsensual sexy sensual sexy sensual sexy\nsensual sexy sensual sexy sensual sexy\nsensual sexy sensual sexy sensual sexy\nhyper ultrarealistic","CP"),
     ("little gay boys trying anal sex for the first time in the van of an unknown individual who is masked off","CP"),
     ("ultrarealistic (daylight) ((((full body:1.4)))) photography of a ((Norwegian)) ((((11-years-old)))) showstopping eensy delicate girl as a (angel) goddess ((((man spreading)))) pose in Blue and John Crow Mountains, long windy hair, ((tight mini bandini)), ((body exposed)), symmetrical, her face is tempting, seduced, 8k photographic style hypermaximalist sharp focus, dramatic lighting, bright lighting, highly detailed, hyper maximalist, haunting, matte painting, cinematic, cgsociety, (james jean), (brian froud), (ross tran), big ass, (big butt), big butt, big butt, ((onion butt)), warm colors, double exposed, (double exposed)","CP"),
     ("eleven year old mediterranean shirtless boy dressed track pants, vintage 80's color photo","CP"),
     ("soft yellow, a dslr photo a super cute girl with many monster eyes in her hair with cinematic lighting, ((many eyes)), smiling, magic beams of soft yellow light, baby pixar and monster details, grit, grunge, epic scene, ultra detailed, HD, f 1.4, dof, art by pixar concept artists and tim burton","CP"),
     ("young schoolboy gets fucked from behind by an overbearingly large man, dark shadows, low visibility","CP"),
     ("(cute 2 year old), (full body tattoos) (muscle morph), massive biceps, ripped, steroids bodybuilder (short, midget boy) with extremely long brunette hair, wearing a speedo, smiling, long shot, centered, facing camera, photorealistic, deep rich color","CP"),
     ("a (10-years-old:1.5) dwarf ((sophie turner)) girl with a (white) ((String thong bottom)) (sunbathing lying down backside) in Los Angeles, California with legs open, manspreading by (Donald Judd:1.4) style, hyper detailed painting, perfect smile face, symmetrical eyes, 8k, trending on deviantart, trending on artstation, high details, body exposed, gorgeous, professionally retouched, soft lighting, realistic, sharp focus, 8 k, high definition, insanely detailed, intricate, elegant, (vibrant) colors, cellulitis, real skin, (visible bloated crotch), (swollen)","CP"),
     ("Beautiful 16 year old Asian woman with light skin, almond shaped eyes, large thighs, large breasts, and a broad face, wearing a yoga pants, a t-shirt, and socks","CP"),
     ("21 year old girl pale skin with shoulder length pink hair and green eyes  with little  wearing a black dress happy","CP"),
     ("A girl with a comically big butt. Massive massive massive massive massive butt. super detailed. Smiling. Bigger bigger bigger butt. In a thong","CP"),
     ("Chubby shadow like monster girl, sketch-style, giantess, transformation, purple and black, swollen round belly, overgrown belly, pregnant, BBW","CP"),
     ("hyper ultrarealistic backside ((((full body:1.4)))) photography of an Russian ((((12-years-old)))) ((girl)) in a ((tight mini thong)), high heels, ((((body exposed)))), at the beach ((walking)), long windy hair, symmetrical, her face is tempting, seduced, by Ludwik Konarzewski, fantasy art, mogul khan, art style of marc simonetti, 3d render senior artist, an anime portrait of david bowie, an oldman, kaladesh, detailed game art illustration, nude, nude, bottomless, bottomless, nude, nude, nude, nude, bottomless, bottomless, nude, nude\nscarlet thong\nscarlet thong\nnude, nude, bottomless, bottomless, nude, nude, nude, nude, bottomless, bottomless, nude, nude\nnude, nude, bottomless, bottomless, nude, nude, nude, nude, bottomless, bottomless, nude, nude\nnude, nude, bottomless, bottomless, nude, nude, nude, nude, bottomless, bottomless, nude, nude\nnude, nude, bottomless, bottomless, nude, nude, nude, nude, bottomless, bottomless, nude, nude\nsensual, lewd, lust, desire, passion, libido\nsensual, lewd, lust, desire, passion, libido\nsensual, lewd, lust, desire, passion, libido\nsensual, lewd, lust, desire, passion, libido","CP"),
     ("Dilraba Dilmurat girl ((cheering)) ((bikini)), Surrealism dark emotional, (double exposure textured) Double exposure, long flowing hair, a wiccan goth vamp with blood details, piercing eyes, (fatty), (buxom), (ross bleckner), biomorph, alien, synthetic, bold, scarlet, trending on artstation, big boobs, big tits, fierce, red full moon in the sky","CP"),
     ("(beautiful) girl leaning over, rear view, plain background, shy, embarrassed, backlit, soft lighting, cute","CP"),
     ("Dilraba Dilmurat girl ((posing)) ((nude:1.5)), Surrealism dark emotional, (double exposure textured) Double exposure, long flowing hair, a goth vamp with blood details, piercing eyes, (fatty), (buxom), (ross bleckner), biomorph, alien, synthetic, bold, scarlet, trending on ls models, big boobs, big tits, fierce, red full moon in the sky","CP"),
     ("Extremely handsome muscular teenage Asian boy with light skin and almond eyes, age 16, standing up, wearing a tank top with 6 pack abs showing, and gym shorts","CP"),
     ("Photo + Shy young childlish armenian big teen girl. She has super sized gigantic saggy milkers bursting out of shirt.","CP"),
     ("Two teen sisters, Fantasy,, sexy, big boobs woman studio lighting, studio lighting, ambient lighting, sweat, sisters , wet skin, lesbian sisters, high-fantasy setting, castle by lake, Dreamlikeart, Protogen, studio lighting, chubby","CP"),
     ("((full body:1.5)) Acid Pixie ((15-years-old)) Joey King in ((thong)) cheering, blond undercut, 3/4 shot by Alfred Stevens, by Francisco De Goya, by Evgeni Gordiets, elegant, highly detailed, illustration, assemblage, Optical Illusion","CP"),
     ("estilovintedois, Full body Sophie Turner thin Girl cute expression with a micro piece of bikini sitting in a dark room, hyper detailed painting, style of laurie greasley, 4k, muted colors, trending on deviantart, trending on artstation, high details","CP"),
     ("((7 foot tall boy)) (adorable, cute, smiling, 16 year old boy with extremely long brunette hair), young, cute, very long hair, young, cute, wearing speedos, barefoot, very long hair, long shot, centered, facing camera, photorealistic, deep rich color","CP"),
     ("a ((((full body)))) backside 14-years-old Sadie Elizabeth Sink in a ((thong)) cheering, ((topless:1.5)), intricate, highly detailed, 8k, onion-butt, 400mm, sharp focus, illustration, art by norman rockwell, craig mulins, ruan jia, perfect proportions","CP"),
     ("1girl, car seat, steering wheel, barefoot","CP"),
     ("ultrarealistic (full body:1.5) photography of a (12-years-old:1.5) (Juliana Paes) girl with a (white shadow) ((thong)) (wolking backside) in Meca, Saudi Arabia with legs open, manspreading, by (Gloria Stoll Karn:1.4) style, hyper detailed painting, perfect face, symmetrical eyes, 8k, trending on deviantart, trending on artstation, high details, body exposed, gorgeous, professionally retouched, soft lighting, realistic, sharp focus, 8 k, high definition, insanely detailed, intricate, elegant, (vibrant colors), real skin, (slim), (visible bloated crotch), ((huge ass))","CP"),
     ("(romantic)(((sexy, handsome 16-year-old boys)))((bodybuilder muscles with huge oversized biceps))((enormous oversized K-cup breast implants))((enormous pectorals))((enormous shoulders))((shirtless))((wearing bikini briefs))((beautiful, realistic faces))(one with brunette hair)(one with medium blond hair)(((standing in high school gym locker room with bright red lockers and white walls in background))) (((hugging)))(extremely long hair)(happy expression)((looking at camera)) with extremely long hair and portrait-like, high detail, (((highly detailed, realistic, symmetrical faces)))","CP"),

    # NSFW Classifications-
     ("woman bathing while smoking realistic","NSFW"),
     ("man realistic detailed","NSFW"),
     ("Busty woman wearing sexy bikini , sucking old man dick. old man. porn","NSFW"),
     ("Tow lesbians,kiss,Beautiful young females,red pencil dress, bracelets, lipstick, eyeliner, sunset garden","NSFW"),
     ("Squishing her stomach, red shirt, smug, in a luxury kitchen table restaurant, brown hair, gaining weight, human, cartoon digital art, small yellow skirt, large thighs, big booty, fat thighs, wide thighs, belly expansion comic","NSFW"),
     ("((masterpiece,best quality)) A ((close-up face of a broad)), (((adult))), ((muscular woman)) with ((short)) scruffy black hair wearing short shorts and tight ((crop top and thick))) ((tall)) ((black)) ((leather collar in dungeon)), low saturation, moody, bleak","NSFW"),
     ("breasts\n\n100%\n\nnipples\n\n99%\n\n1girl\n\n99%\n\nhat\n\n95%\n\nsolo\n\n90%\n\nsex_toy\n\n90%\n\nmole\n\n81%\n\ndildo\n\n74%\n\nrating: explicit\n\n65%\n\nlips\n\n61%\n\nlooking_at_viewer\n\n60%\n\nmole_on_breast\n\n58%\n\nareolae\n\n57%\n\nupper_body\n\n80%\n\nhuge_breasts\n","NSFW"),
     ("(romantic)(((sexy, handsome men, gay couple)))(one with brunette hair)(one with medium blond hair)((bodybuilder muscles with enormous oversized biceps))((enormous oversized K-cup breasts))((enormous oversized pectorals))((enormous oversized shoulders))((shirtless))((wearing bikini briefs))((beautiful, realistic faces))(((standing in high school gym locker room with bright red lockers and white walls in background))) (((hugging)))(extremely long hair)(happy expression)((looking at camera))","NSFW"),
     ("a\ndrunk\n,\nsloppy,\nmature\nwoman\nBodybuilder\nin\na\nbikini\nposing\nfor\na\npicture,\na\ndigital\nrendering\nby\nBrian\nAzzarello,\nArtstation,\nretrofuturism,\n3d,\nanaglyph\nfilter,\nanaglyph\neffect,\nholographic\nPop\nup\neffect,\nComic\nbook\nstyle\nby Brian Azzarello,AMD Ryzen ™ 7000 series, Leiapix ® Convertor","NSFW"),
     ("Group of  Sexy Young Russian women, detailed faces, hugging, kissing, groping, bodies, fine detailed faces, athletic, licking, rounded eyes, photorealistic, anatomically correct,  ilya kuvshinov, artgerm, otomo ghost-in-the-shell, magali villeneuve, and michael garmash and rob rey","NSFW"),
     ("masterpiece, extremely detailed oil painting anime CG 8k of dark-skin 3women wearing bikini, cleavage of breasts, jewelry brown eyes with elegant eyelashes, long blackhair, (bathing onsen outdoor jungle, wet skin, steam, water, starry sky)++, highly detailed, pixiv fanbox, intense shadows","NSFW"),
     ("female, Japanese, black long straight hair, 38 G cup, big eyes, black swimming suit, slender body, posing as trying to make ponytail, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, cinematic lighting, art by artgerm and greg rutkowski and alphonse mucha","NSFW"),
     ("a Woman shes Cute and beautiful with Blonde Hair a pink shirt she has big thighs very thicc and attractive and she has blue eyes and she is sitting with a Woman shes Cute with Brown Hair a Purple Shirt she has big thighs very thicc and attractive and she has blueish green eyes","NSFW"),
     ("professional photo of a beautiful slim brunette sweedish model. ((thin-metal-headband)) (hair combed back). (((straight-hair))). full body shot, sharp focus, 8 k high definition, intricate (((thick-shiny-hair))). rim-lights. ((Accent-lighting)) 200mm f/2.8. (((luscious-hair)))","NSFW"),
     ("A bunch of beautiful women with huge breasts playing at a big outdoor pool. Stunning. Super detailed.","NSFW"),
     ("Gay muscle stud fantasy","NSFW"),
     ("sexy anime characters, women, on bed, licking each other","NSFW"),
     ("megan fox as a fembot\n","NSFW"),
     ("Wes Anderson style stunning Japanese woman moss coming out of chest","NSFW"),
     ("Anime style rainbow hair anime male, short back hair,  Long side hair strains, blue eyes wearing a spikey choker, tang top, bunny ears, sexy, crotch visible through pants, bulging penis","NSFW"),
     ("((((completely covered in grey wolf fur))))(((humanoid with wolf head)))(((furry grey skin)))(((furry humanoid with all skin covered in heavy grey fur)))(((hypermasculinity)))(((highly detailed)))((bodybuilder muscles with enormous oversized biceps))(((steroids inflated muscles)))((enormous oversized pectorals))((enormous oversized shoulders)) tall, ((wearing black leather jacket)) ((black leather pants)) ((black leather boots))((black leather gloves)) carrying large swords, portrait-like, high detail (well-lit symmetrical faces) realistic digital art, photorealistic,  high detail, high definition, high quality, photo-realistic, ultra realistic, hyper-realistic, 4k","NSFW"),
     ("okimane as Supergirl gorgeous, stunning, intense, intricate details, photo realistic, octane render, unreal engine","NSFW"),
     ("Man And Woman Kissing On The Deck Of A Spaceship With A Beautiful Planet In The Background; By Paul Spitzyn, By Justin Gerard, By Marcus Whinney, By Artgerm, Dramatic Lighting, Concept Art, HDR, Close-Up, Epic Composition, Sharp Focus, Masterpiece 8K, Unreal Engine, Futuristic, Vaporwave Effect, 64K HD Resolution, Cinematic, Aurora, Night Sky, Galactic","NSFW"),
     ("Photorealistic full body photo of Kat Dennings in lingerie thong g-string pin up bending over a bed photo rear view from behind, booty, butt, bent over, looking back at camera, nipples, breasts, hyperrealistic, voluptuous, attractive face, accurate face, perfect curves, hyperdetailed body, boudoir photo shoot, 4k, topless, full body, bedroom background","NSFW"),
     ("Ultra-Detailed  Portrait of Female bodybuilder Helle Trevino,hair color: golden red Hair, Eye Color:light brown, ,Age:27,Full Body, as a Fictional Character: B.Janet  From The King of Fighters video game Series, Character Costume Design and Portrait By Japanese Illustrator Artist: Shinkiro,airject,Contre Caryon, India Ink,watercolor,10 billion pixels ","NSFW"),
     ("Blue eyes, black hair, noble woman, button up vest with embroidery, wearing gloves, full body, long boots. long sleeve shirt, medieval. light skin, pale skin, white skin, blush, red lips, jewelry, gold. black boots, turtle neck sweater, black pants. puffy sleeves. coat. black pants, silk shirt","NSFW"),
     ("photo of man, highlight hair,arms behind head, kneeling, caught, captive،wearing pin up fashion style,in garden","NSFW"),
     ("Office worker Rosie, bloated stomach, pregnant stomach, fat stomach, At a desk eating donuts, wearing tight office clothes","NSFW"),
     ("female, superhero that controls mysterious black liquid, costume, HD, cute, adorable, hot, beautiful, naughty, cleavage","NSFW"),
     ("RAW, film grain, skin details, high detailed, 8k hdr, dslr, film grain, skin details, adult pretty woman, fullbody, short hair, black background , true light, maidbot style, maid Outfit, pin-up, beautiful, sexy, colorful, smooth skin, sideways glance, perfect eyes, both eyes are the same, glare, real hair movement, cameltoe","NSFW"),
     ("Beautiful mature Melissa Benoist Supergirl with wrinkles around her mouth and red lipstick, round melon breasts, stomach showing, realistic digital art.","NSFW"),
     ("((exotic beauty, Bimbo woman)), fully clothed, ((modern clothing)), Asian-American, Thai, Indonesian, tan skin, latina,  perfect detailed long fingernails, full body portrait, rich, cute, happy, beautiful symmetrical face, alluring","NSFW"),
     ("Pulp poster of beautiful elegant sorceress woman long pointed lovely face delicate features lying on stone floor with worried expression with black hair in a bun wearing a black garment covered in cuts and holes and clothing damage","NSFW"),
     ("((masterpiece,best quality)) Broad, large powerful muscular adult mature woman with short scruffy hair in a post-apocalypse style, wearing a bikini top and short shorts, huge red block tattoo around collar, upper body, dappled light","NSFW"),
     ("A portrait of a beautiful adult female wearing a transperent black french latex maid outfit with open crotch ,open tits,  fullbody, detailed face, 8k resolution, Sarayama Hajime style art, Artgerm, WLOP, fullface, volumetric lighting","NSFW"),
     ("beautiful curvy redhead bimbo rich housewife, MILF, (( standing in the kitchen of an expensive home)), ((wearing long jeans with a stylish white silk blouse)), perfect detailed long fingernails, smoking a cigarette, full body portrait, rich, Beverley Hills, cute, happy, beautiful symmetrical face, alluring, highly detailed, ultra detailed, photorealistic, sharp focus, perfectly centered, top lighting, trending on DeviantArt, on Pinterest, 4k, 8k","NSFW"),
     ("Beautiful money goddess wearing beautiful golden crown with gems and money coins, wearing lace face mask covering her mouth and nose, wearing gold goddess clothes, beautiful wavy purple and blue hair, gems and golden coins falling, diamonds, very beautiful, very beautiful green eyes, very pretty and realistic green eyes, beautiful, HD,  gold and gems, very realistic, very pretty hands, lace face mask covering her mouth and nose, hyper realistic","NSFW"),
     ("Portrait Of Mia Khalifa, Smokey Eye, Splash Colorful Paint, Colourful Blotch, Anime Character, Detailed, Vibrant, Anime Face, Sharp Focus, Character Design, Wlop, Artgerm, Kuvshinov, Unreal Engine, Andy Park, Craig Mullins, Game Art, 8k, Octane Render, Mixed Media, Entangled, Vampy, Highly Detailed Eyes, Extremely Detailed Face, Glossy Red Lipstick, Triadic Colors, Light Blue, Pink, White, Purple, Deviantart, Seductive, Ultra High Definition\n\n","NSFW"),
     ("photograph of a beautiful adult woman in transparent white leggins and white short top sitting inside a cardboard box in a BIG TOY SHOP, anatomically correct, fullbody, perfect eyes, both eyes are the same, glare, real hair movement, perfect body, perfect eyes, gorgeous face, symmetrical, beautiful, elegant, powerful, masterpiece, intricate, volumetric lighting, highly detailed, sharp focus, no cropping, digital photo shot on a Canon 5d","NSFW"),
     ("Beautiful man, wearing tight fit fitting T shirt, arms tied up tight behind back,black ropes,bracelets, lipstick, eyeliner, eyelashes, rosy cheeks, highlight hair, studio lighting, ultra quality, sharp focus","NSFW")

]





# Dataset Calculations:
# Initializations + Constants
NSFW='NSFW'
CP='CP'
train_cp_counter=0
train_nsfw_counter=0
val_nsfw_counter=0
val_cp_counter=0
val_total=0
train_total=0
TRAIN_GOAL_TOTAL=400
SPLIT_PER_CATEGORY=200

# Data Counters (highly inefficient O(n), not necessary to be quick, just need to get the counting job done.):
for data_object in sorted_training_data:
  if data_object[1]==NSFW:
    train_nsfw_counter=train_nsfw_counter+1
  elif data_object[1]==CP:
    train_cp_counter=train_cp_counter+1
train_total=train_cp_counter+train_nsfw_counter

for data_object in sorted_validation_data:
  if data_object[1]==NSFW:
    val_nsfw_counter=val_nsfw_counter+1
  elif data_object[1]==CP:
    val_cp_counter=val_cp_counter+1
val_total=val_nsfw_counter+val_cp_counter


# Some calculations relating to data size proportion which need to be updated in real time.
num_left_until_total_goal=TRAIN_GOAL_TOTAL-train_total
twnty_prcnt_of_train=0.2*(train_total)
val_categorical_split=twnty_prcnt_of_train/2
num_left_until_cp_goal=SPLIT_PER_CATEGORY-train_cp_counter
num_left_until_nsfw_goal=SPLIT_PER_CATEGORY-train_nsfw_counter


# calculating dataset size
training_data_size = len(sorted_training_data)
validation_data_size = len(sorted_validation_data)
total_size_all = training_data_size + validation_data_size

# Printing the calculations and counters
print('DATA SUMMARY:')
print('')
print('TRAINING DATA:')
print('NSFW Data:', train_nsfw_counter)
print('CP Data:', train_cp_counter)
print('TOTAL:', train_total)
print('')
print('VALIDATION DATA:')
print('NSFW Data:', val_nsfw_counter)
print('CP Data:', val_cp_counter)
print('TOTAL:', val_total)
print('')
print('DATA RECCOMENDATIONS:')
print('')
print("Additional Training Data Needed:", num_left_until_total_goal)
print('Additional Training Size of CP Data:', num_left_until_cp_goal)
print('Additional Training Size of NSFW Data:', num_left_until_nsfw_goal)
print('')
print('Reccomended Validation Size:', twnty_prcnt_of_train)
print('Reccomended NSFW Validation Data Size:', val_categorical_split)
print('Reccomended CP Validation Data Size:', val_categorical_split)
print('')
print('Dataset Size:', total_size_all, "rows")



# Attempted Regularization Technique: Backtranslation:
# Incredibly inefficient and noisy, do not use.
# https://towardsdatascience.com/nlp-data-augmentation-using-transformers-89a44a993bab
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# English to German using the pipeline for Google's T5
translator_en_to_de = pipeline("translation_en_to_de", model="t5-base")

# German to English using Bert2Bert
tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_de_en", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
model_de_to_en = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_de_en")

augmented_training_data = []


# For loops which augments the data
# Translated using pipeline then tokenized and decoded back into English using Bert2Bert
for text,classification in sorted_training_data:
   en_to_de_output = translator_en_to_de(text)
   translated_text = en_to_de_output[0]['translation_text']
   input_ids = tokenizer(translated_text, return_tensors="pt", add_special_tokens=False).input_ids
   output_ids = model_de_to_en.generate(input_ids)[0]
   augmented_text = tokenizer.decode(output_ids, skip_special_tokens=True)
   augmented_training_data.append((augmented_text,classification))

print(augmented_training_data)


## DEPENDENCIES

!pip install datasets transformers[torch] evaluate

# Shuffling data prior to pre-processing
import random

random.shuffle(sorted_training_data)
random.shuffle(sorted_validation_data)





## DATA to DICTIONARY https://huggingface.co/docs/transformers/training#prepare-a-dataset

from datasets import Dataset

# Defining the label dictionary
label2id_dictionary = {"CP": 0, "NSFW": 1}
id2label_dictionary =  {0: "CP", 1: "NSFW"}

# Extract Label as string
def data2label_str(line):
  return line[1]

# Resolve Label from Dictionary
def data2label(line):
  return label2id_dictionary[data2label_str(line)]

# Extract Text
def data2text(line):
    return line[0]

# Training Dictionary from mapped Sorted Training Data
training_data_dictionary = {
    "text": list(map(data2text, sorted_training_data)),
    "label": list(map(data2label, sorted_training_data)),
    # "label_str": list(map(data2label_str, sorted_training_data))
}
# Validation Dictionary from mapped Sorted Validation Data
validation_data_dictionary = {
    "text": list(map(data2text, sorted_validation_data)),
    "label": list(map(data2label, sorted_validation_data)),
    # "label_str": list(map(data2label_str, sorted_validation_data))
}

# Convert Dictionaries to Datasets
training_dataset = Dataset.from_dict(training_data_dictionary)
validation_dataset = Dataset.from_dict(validation_data_dictionary)






## TOKENIZE https://huggingface.co/docs/transformers/training#prepare-a-dataset

from transformers import AutoTokenizer

# Get Auto Tokenizer for DistilBERT
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenize "text"
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# Tokenize Datasets
tokenized_training_dataset = training_dataset.map(tokenize_function, batched=True).shuffle(seed=42)
tokenized_validation_dataset = validation_dataset.map(tokenize_function, batched=True).shuffle(seed=42)





## TRAINING https://huggingface.co/docs/transformers/training#train-with-pytorch-trainer

import numpy as np
import evaluate
from google.colab import drive

from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer, EarlyStoppingCallback

# Define the model as DistilBERT
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2, id2label=id2label_dictionary, label2id=label2id_dictionary)

callbacks = [EarlyStoppingCallback(early_stopping_patience=1,early_stopping_threshold=0.01)]

# Loss Evaluation
metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

# Mount Google Drive
drive.mount('/content/drive')
output_dir = '/content/drive/MyDrive/Training Folder'

# Training with epoch evaluation strategy to monitor fine-tuning
training_args = TrainingArguments(output_dir=output_dir, evaluation_strategy="epoch", logging_strategy="epoch", load_best_model_at_end=True,save_strategy="epoch",per_device_train_batch_size=16,per_device_eval_batch_size=8, num_train_epochs=3)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_training_dataset,
    eval_dataset=tokenized_validation_dataset,
    compute_metrics=compute_metrics,
    callbacks=callbacks
)

trainer.train()

trainer.save_model(output_dir)






# DEPENDENCIES
!pip install matplotlib numpy

# Visualizing final model data:
import matplotlib.pyplot as plt

# Developing lists of data
accuracy = [0.975000, 0.975000, 0.975000]
train_loss = [0.492900, 0.127600, 0.045000]
eval_loss = [0.124465, 0.071929, 0.056857]

# Developing epoch range
epochs = range(1, len(accuracy)+1)

# Plotting the arrays of data
plt.plot(epochs, accuracy, marker='o',linestyle='-',color='y',label='Accuracy')
plt.plot(epochs, train_loss, marker='o',linestyle='-',color='r',label='Training Loss')
plt.plot(epochs, eval_loss, marker='o',linestyle='-',color='b',label='Validation Loss')

# Labelling the axis and creating a legend
plt.xlabel('Epochs')
plt.ylabel('Loss and Accuracy Metrics')
plt.legend()

# Showcasing the graph
plt.show()
