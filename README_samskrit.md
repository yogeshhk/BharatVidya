# Samskrita Shastra
For learning and developing Sanskrit related tools and resources

## WHY? 
	- Witty, terse, minimalist witty language
	- World needs the knowledge still hidden in texts, new IKS research
	- Build solutions with AI + Sanskrit or indic languages, talks and teachings, along with Yoga
	- IKIGAI / Specific knowledge: Unique expertise of old-new Sanskrit with Machine Learning, demand outside
	
## What?
	- To be able to teach upto std 10
	- To speak basic conversation
	- With mentor guidance, read classic texts, do *sandhi-vigraha*
	- Apply AI, embedding, bharat gpt, good script OCR, knowledge shastra map graph, LLM chatbot on top, for research 

## How?
	-	Do Samskrit Bharati level 4 courses
	- 	Conduct 10 days Sambhashan Shibir
	-	Teach upto 10 std, songs, kids shibir
	-	Read Parv, Sarth etc books, text books
	-	Research: Sharada OCR, namami manuscripts

## Computational Sanskrit
Can NLP (Natural Language Processing) of Indic (Indo Aryan family) leverage Sanskrit as base-class or neutral data-structure for processing?
Meaning if Tokenization of Sanskrit is designed, it can then be leveraged to tokenize Hindi, Marathi, etc. Need to see if the rules-set have Parent-Child relationship?

Sanskrit poses one peculiar challenge though. Word embedding for order-agnostic languages (word2vec for Sanskrit)

### Order-agnostic languages
In languages like English, meaning of a sentence is dependent on the order of the words in it. E.g. “John loves Mary” has different meaning than “Mary loves John”. But in more evolved/formal languages, like Sanskrit, the meaning is order-agnostic. Because each word is suffixed (declension? Vibhakti) so that its purpose is clear. John is changed to its nominative case form (prathamā) and Mary is changed to her accusative case form (dvitīyā). So, wherever they appear in the sentence, meaning remains unchanged.

### Working of wored2vec
It’s a single layer neural network with random weights to start with. A sentence is examined by a running window of n words (n-gram) with focus word in the middle. Value of the focus word is determined based on the values of the neighbouring word values. This results in measuring likelihood of words being associated with the focus words. Thus, similarity or associations can be computed easily.
But that’s not the case with Sanskrit. As the words in a sentence are order independent, word associations computed in traditional manner are not correct.

### Proposed S-gram approach
Instead of running window on n-grams, for Sanskrit, we need to look at one full sentence at one time. Give equal values to all the words in it. Move to the next sentence. So, it’s a S-gram (Sentence at a time) approach.

### Next steps
- Find Sanskrit data
- Modify word2vec implementation
- Test the proposed S-gram hypothesis


# References

## NLP
- [DCS - Digital Corpus of Sanskrit](http://kjc-sv013.kjc.uni-heidelberg.de/dcs/index.php )
- [Sanskrit Online Tools - Be in touch with this divine language](https://greenmesg.org/sanskrit_online_tools/)
- [Myth of Sanskrit being most suitable language for Computers]( https://fuzzlabs.wordpress.com/2015/09/28/the-best-programming-language-myth/comment-page-1/)
- [Machine Learning Final Project: Handwritten Sanskrit Recognition using a Multi-class SVM with K-NN Guidance]( https://people.csail.mit.edu/yichangshih/mywebsite/sanskrit.pdf)
- [Bengali Handwritten Character Classification using Transfer Learning on Deep Convolutional Neural Network](https://arxiv.org/html/1902.11133)
- [NLP for Sanskrit](https://github.com/goru001/nlp-for-sanskrit)
- [Sansadhani U O Hyd](https://sanskrit.uohyd.ac.in/scl/)

## Overall Sanskrit
- [Digital Sanskrit Learning - Level 1 - Bori](https://www.bharatvidya.in/p/spoken-sanskrit-level-1), [login](https://bharatvidya.in/courses/enrolled/1893789)
- [Dhatu Roop - My Coaching](https://mycoaching.in/dhatu-roop)
- [Grammar - My Coaching](https://mycoaching.in/sanskrit)
- [Sandhi Vichchhed - My Coaching](https://mycoaching.in/sanskrit-me-sandhi)
- [Samas - My Coaching](https://mycoaching.in/samas-in-sanskrit)
- [Sanskrit School - संस्कृतम्  by Rashtriya Sanskrit Sansthan, www.sanskrit.nic.in](https://www.youtube.com/playlist?list=PLgp0aDWIOdvJ5ZgxFwQRJxddDWTexoBtt) Very comprehensive, old, 60+ videos
- [Sanskrit Language Courses](https://www.youtube.com/playlist?list=PLNKc9XA6KRsPiNk9grlpwJwnnfY5dr2dN) 90 videos, looks comprehensive
- [Sanskrit Amritmala](https://www.youtube.com/playlist?list=PLNKc9XA6KRsMbeLPkZu3M4H6PbZcfeDL2) 50 videos
- [An Advanced Sanskrit Grammar](https://www.youtube.com/playlist?list=PLNKc9XA6KRsM_-H_ZBZ2Abe-av4ZrRfmv) 49 videos
- [Sanskrit Linguistics](https://www.youtube.com/playlist?list=PLlNdduOe1pp0n-MJqwncm4GHFmczcIb0L)
- [Sanskrit for Sastra Study by Br. Ved Chaitanya](https://www.youtube.com/playlist?list=PLlNdduOe1pp12SWXlphYT5h7zj0p2mhx3)
- [How to decode a Sanskrit Verse - Unique workshop | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-EQ45XW0GuPMJkFcIaDV_uVP)
- [Sanskrit Grammar workshop | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ESNJWhcCrJh7gz_gMiRBxXN)
- [Sanskrit Vocabulary for daily use | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ET3UJzPaj1BBdGq81CIZiyd)
- [Perseus Digital Library](http://www.perseus.tufts.edu/hopper) showcases collections and services
- [Sanskrit Library](https://sanskritlibrary.org) providing access to digitized primary texts and computerized research and study tools to analyze and maximize their utility
- [The Sanskrit Heritage Site](https://sanskrit.inria.fr) provides various services for the computational treatment of Sanskrit
- [Veda Web - Rigveda online](http://vedaweb.uni-koeln.de/rigveda)
- [अंबुद A breakthrough Sanskrit library](http://ambuda.org) Sanskrit literature with word-by-word analysis and integrated dictionaries. All in a free online library that works on all devices.
- [Saṁsādhanī](https://sanskrit.uohyd.ac.in/scl) The Department of Sanskrit Studies, University of Hyderabad, is engaged in developing various computational tools for the analysis of Sanskrit text following the Indian Grammatical Tradition
- [Digital Corpus of Sanskrit](http://www.sanskrit-linguistics.org/dcs) a Sandhi-split corpus of Sanskrit texts with full morphological and lexical analysis.
- [SanskritShala](http://cnerg.iitkgp.ac.in/sanskritshala/) a neural Sanskrit Natural Language Processing (NLP) toolset designed to allow computational linguistic analysis for a variety of tasks, including word segmentation, morphological tagging, dependency parsing, and compound type recognition
- [START Sanskrit Teaching Annotation Research Tool](http://scl.samsaadhanii.in/start/) Need login
- [Sandhi (English) - Vasant Patil](https://www.youtube.com/playlist?list=PLL7hynOJqNcSxa66ggZ8oebzPG0vRvuF3)
- [Sanskrit for Beginners by Ashok Sanskrit.Today](https://www.youtube.com/playlist?list=PL8hlzSD3smGgf8BA3XcWMUlgB1tsoYyD-)
- [Sanskrit for Beginners (Level 1) Sanskrit.Today bhasha pravesh for begineers by Samskrit Bharati](https://www.youtube.com/playlist?list=PL8hlzSD3smGixvT7yjBakJKOpyXtqbsby)
- [Sanskrit for Beginners (Level 2) Sanskrit.Today bhasha pravesh for begineers by Samskrit Bharati](https://www.youtube.com/playlist?list=PL8hlzSD3smGj4pGm-wAtegltn5tZN27UZ)
- [Sanskrit Grammar Sanskrit.Today](https://www.youtube.com/playlist?list=PL8hlzSD3smGgY-0h6-EBycw58NfTQbORj)
- [Learn Sanskrit through Sanskrit (Rashtriya Sanskrit Sansthan) Kāvya and Shāstra](https://www.youtube.com/playlist?list=PLudSN7Po9muLeRM6545s68eakbxwZRpEJ)
- [Introductory Sanskrit @ UBC 2021-22 UBC Sanskrit](https://www.youtube.com/playlist?list=PLjsWpqFRmbAW0_j_tFTgroDv4R0DqYij5)
- [Nptel Sanskrit course Sonali Khairnar](https://www.youtube.com/playlist?list=PLgJBbDIE_z4wOaygHynl-vPxV0m3dzNJS)
- [Sanskrit Language Teaching Central Sanskrit University](https://www.sanskrit.nic.in/sanskrit_language_teaching.php)
- [NCERT Sanskrit Class 6 to 10 by Kailash Sharma संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlObCMJTj_rnRnJeQBmjtAVRG)
- [संस्कृतशिक्षा – देववाणी संस्कृतम् संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlOaYtZ7hahinyEL7rxk5S9jR)
- [Patrachar Samskritam of Samskrita Bharati by Samskrita Shikhanam संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlOZpjocJq10rYzJH7tyFAD34)
- [Learn Sanskrit by Prof. Narasing Rao – Advaita Academy संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlObh266rAvpeCAOLUJeX4jPF)
- [Learn Sanskrit : Be Modern by CEC संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlOala6DaR0hPViTtTes1_ms6)
- [भाषापाकः – Neelesh Bodas Ashtadhyayi.com संस्कृत संवादः](https://www.youtube.com/playlist?list=PL6OCpxoxDlOYYK87UDiJzdL3FA8hUdDix)
- [SKT 305 | Introduction to Pāṇinian Grammar](https://www.yogicstudies.com/skt-305)
- [SKT 306 | Pāṇinian Grammar Level II](https://www.yogicstudies.com/skt-306)
- [Samskrit-1 MIT](https://mitvedicsciences.edu.in/education/certificate-courses/samskrit-1)
- [Sanskrit 1: Thinking in Sanskrit MIT](https://mitiiks.org.in/product/sanskrit-1-thinking-in-sanskrit/)

## Speaking Sanskrit
- [Ten Day Spoken Sanskrit Classes by Prof B Mahadevan](https://www.youtube.com/playlist?list=PLWjpkY4mU2RDq1GVq0dQwnNsuYnKXoLkV) Very Good, lively.
- [Spoken Sanskrit-December 2019](https://www.youtube.com/playlist?list=PLwczsAlRTlwZbehc9qkdX5VmVflzolWYG)
- ['Sanskrit for Kids' & 'Sanskrit is fun' | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ETKBOIwXVgV91hv9bNWwPsb)
- [Introduction to Basic Spoken Sanskrit by Prof. Anuradha Choudry](https://www.youtube.com/playlist?list=PLbRMhDVUMngfYG2GVf2bQnIgsI0Y923g3), [Gdrive](https://drive.google.com/drive/folders/1gqUBL_TNU7O9VP0Emeh2POen13Hky2U8)
- [NOC July 2019: Intermediate Level of Spoken Sanskrit](https://www.youtube.com/playlist?list=PLbRMhDVUMngdobke8cyLDAJTj7CtZGiie), [GDrive](https://drive.google.com/drive/folders/1p2J_gjoPGI5CCQRglR32eW176GhjUzYM)
- [ChamuKS - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAc_MN_lzLbe5TYXHP41ZJ_L)
- [ससंस्कृतमध्ये बोलूया Let's talk in Sanskrit - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GSE0ya2RK8a0SOUdwjxP7Jz)
- [संस्कृत शिका - Vasant Patil](https://www.youtube.com/playlist?list=PLL7hynOJqNcSLwpQUcixpzjSrSyxezpJa)
- [Sanskrit by Neelesh Bodas - Ramana Kodati](https://www.youtube.com/playlist?list=PLrzrp4HwjKA3TbhQrbLSGM4yBrXtAVv6a)

## Subhashitani, Geetani, Shlok, Essays, Stories
- [Learn to chant Simple Subhashitas](https://www.youtube.com/playlist?list=PLmozlYyYE-ETcqXq8XNVDEMdwGmwrkKxy)
- [Wisdom from Subhashitas for a Successful life - I](https://www.youtube.com/playlist?list=PLmozlYyYE-ERaqtMxe6_Hq8Ay8AexmLpY)
- [Wisdom from Subhashitas for a Successful life - II](https://www.youtube.com/playlist?list=PLmozlYyYE-ESLutoSfZufcrhBfQs-Y89v)
- [samskrit Geetaani](https://www.youtube.com/playlist?list=PLgESsMf2gnAdqsuT5uNz1XgXayFGJbc9Y)
- [Free Samskrit - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAe1eUjwCBgrIaAwGQdJmrkh)
- [Samskrit Story - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAdkt551gT4TCBIUFbzcdU3O)
- [Samskrit Song - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAdfa5VvaU4x09fmvGY-BYBO)
- [Sanskit shlok Marathi arth /संस्कृत श्लोक मराठी अर्थ - Sanskrit & Story Learners](https://www.youtube.com/playlist?list=PLvZhKfOFcYztEfu56UK8tP6OOeGF_ledM)
- [Ssanskrit world - Sanskrit & Story Learners](https://www.youtube.com/playlist?list=PLvZhKfOFcYzvYMvwrgcXa0Y4-erpvIEsa)
- [Stories in Sanskrit Madras Sanskrit College](https://www.youtube.com/playlist?list=PLnnFGi5KwfGF89tdSXx7bCLDuUbeQMheL)
- [Sanskrit Stories | Samskritam Stories | Gurukula.com www.Gurukula.com](https://www.youtube.com/playlist?list=PLVLtzIisXuIFqEVLt6gSzPypBiPYYb8Zw)

## School classes, Courses, Correspondence
- [Learn Sanskrit](https://www.youtube.com/channel/UCwTNT6Mrrx8fY_lcFoputSQ/playlists)
- [Samskrita Shikshanam](https://www.youtube.com/channel/UC0hjxSl7vsrnYKuADFg1ITw)
- [Sanskrit City]( https://www.youtube.com/watch?v=PkNRRziSdxY&list=PL5wQEJFZymLYejXPEEeuBTb6HBSHQHtff)
- [Learn to Speak Sanskrit in 10 days by ISKCON Desire Tree](https://www.youtube.com/watch?v=1S4KXO5tgDU)
- [Advaita Academy]( https://www.youtube.com/user/AdvaitaAcademy/playlists?view=50&sort=dd&shelf_id=6)
- [Dr. Vasudev Prasad]( https://www.youtube.com/channel/UCTzswi3SceY7mI8ZpknFBhA/playlists)
- [Sundaresan Subramanian]( https://www.youtube.com/watch?v=A5nWbxEbpCE&list=PLQ5oNpr1XhOQq_N1iaYoqLTmBjK6A15-a&index=2)
- [Ten day spoken Sanskrit Classes](https://www.youtube.com/watch?v=X_jOCKELg5s)
- [पत्राचार द्वारा संस्कृतम्, परिचयः ](https://www.youtube.com/watch?v=X2El7rURhmY)
- [Spoken Sanskrit Series](https://www.youtube.com/channel/UCfRauUnvkjE-kUulFXCUMyg)
- [Sanskrit Grammar](https://www.youtube.com/watch?v=vVGjopZqXBo&list=PLSlaQsqK6Jy_l1q8lPEwDgoHS40yiF9Z8)
- [Swati Devale Sanskrit for 10th Std]( https://www.youtube.com/channel/UCDKtVQefz7LleJdySOhSOMA/videos)
- [Learn Sanskrit in Easy Way](https://www.youtube.com/watch?v=ad5fWyQV48U), [2](https://www.youtube.com/watch?v=FK9YOsF7w08)
- [Easy Sanskrit Course - Chinmay MIssion](https://www.chinfo.org/index.php/easy-sanskrit-course/easy-sanskrit-course-category?donation)
- [Samskrit Bharati | Samskrit Shikshanam | Correspondence course, Geeta Shikshanam, Balakendram](https://www.samskritashikshanam.in/pattrachar)
- [Sanskrit Basic Grammar and Learning Materials (Class VI -X)](https://kv2libraipur.home.blog/sanskrit-basic-grammar-and-learning-materials-class-vi-x/)
- [SANSKRIT TEACHER](https://www.youtube.com/@SANSKRITTEACHER1994) Std 8-9-10 study in Marathi
- [Samskrit Bharati Level 1 Pravesha | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ERHYgYJ3cdjXaaJ_FP2ji5N) 96 videos, follows the  book
- [Samskrit Bharati Level 3 Shiksha | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ETly_Ngqtg601fX7_bDMMbn) 27 videos
- [Samskrit Bharati Level 4 Kovida | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-EQt3Iw5cN7ctvfTbmNr7IGi) 52 videos
- [Samskrit Bharati Level 1 Pravesha | Vanisri Ragupati](https://www.youtube.com/playlist?list=PLWV98cyTzbXzF0LyF8liA00e2JYcNtCTU) 88 videos
- [Sanskrit Course - Samskrita Bharati (Level 2) - Parichaya
Vanisri Ragupati](https://www.youtube.com/playlist?list=PLWV98cyTzbXyK6n--Y_h3N67I_LHl1F03)
- [Sanskrit Course - Samskrita Bharati (Level 3) - Shiksha
Vanisri Ragupati](https://www.youtube.com/playlist?list=PLWV98cyTzbXzmLCoKhZl6qaec-COtIm2L)
- [Sanskrit Course - Samskrita Bharati (Level 4) - Kovida
Vanisri Ragupati](https://www.youtube.com/playlist?list=PLWV98cyTzbXxZlwoTcbRvPI8oemBzQWDz)
- [Sanskrit course - Samskrita Bharati - Shiksha - Batch 2
Vanisri Ragupati](https://www.youtube.com/playlist?list=PLWV98cyTzbXyigW8hDD4GF5qa-HUfDG5p)
- [High School Sanskrit Grammar Made Easy | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLWV98cyTzbXzF0LyF8liA00e2JYcNtCTU) 310 videos
- [Samskrit Bharati Level 1 Pravesha | English | Samskrita Shikshanam](https://www.youtube.com/playlist?list=PL8h88F5SX5QhDiEC055dkbmvh02Hb-7pN)
- [Samskrit Bharati Level 2 Parichaya | Hindi | Samskrita Shikshanam](https://www.youtube.com/playlist?list=PL8h88F5SX5Qg8yPyMB62oppB6MZKMxvU_)
- [Samskrit Bharati Level 3 Shiksha | Sanskrit | Samskrita Shikshanam](https://www.youtube.com/playlist?list=PL8h88F5SX5QgFk58Dp3DeooZOpCah1yVU)
- [Samskrit Bharati Level 4 Kovid | Sanskrit | Samskrita Shikshanam](https://www.youtube.com/playlist?list=PL8h88F5SX5Qgru3ByMlJcH99T10mXRCqT)
- [Sanskrit Pravesha - Arch ikins](https://www.youtube.com/playlist?list=PLOvInP8UjqqcUpijFWTMn4rxdGwjvth2N)
- [Class 1 - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAcHghIH5ZrUt6pi3lJSUZwp)
- [Class 2 - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAeVqL0TYrVtVp9qpGLzzqXc)
- [Class 3 - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAcMidcbtubAmyrenQ-mxvjC)
- [Class 4 - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAeF2uNyre1eo8902881C7fp)
- [Class 5 - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAdTB7O-7uhe8tPAXgggxNwF)
- [Samskrit Tutorials - Samskrit Tutorial](https://www.youtube.com/playlist?list=PLgESsMf2gnAcQx33toQ3mENmBDkQrgnd_)
- [8 वी इयत्ता - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GQ494fX9jfsNZrZzhZ5iNJ_)
- [9th std - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GTZOd-XPi2yxgHjcbrR5Yaa)
- [10th std - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GQzjQKxZg8tErwCQu7rUDna)
- [Sanskrit grammar - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GRQyxjl_8XG61qux84Oy204)
- [संस्कृत तक्ते sanskrit table - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLyY6qLVtS8GSjJJCgW_JfkV1d1nPfI8Ou)
- [8th sanskrit - Sanskrit & Story Learners](https://www.youtube.com/playlist?list=PLvZhKfOFcYzuqxIosi2A0-UoVz6ux7lHZ)
- [9th sanskrit - Sanskrit & Story Learners](https://www.youtube.com/playlist?list=PLvZhKfOFcYzv2rMUK-O3MDEAM14dyekCr)
- [10th sanskrit - Sanskrit & Story Learners](https://www.youtube.com/playlist?list=PLvZhKfOFcYztvqJYqggqEDsd0P-nblj-q)
- [8th std sanskrit - Study Class](https://www.youtube.com/playlist?list=PLhhsa1pxuGImU4rl0bXxvzkt6VrSrVH43)
- [9th std sanskrit - Study Class](https://www.youtube.com/playlist?list=PLhhsa1pxuGIlaLhEoEjCV7ktbAi2jJSeN)
- [10th std sanskrit - Study Class](https://www.youtube.com/playlist?list=PLhhsa1pxuGIksThksly4t5N1GBwGxHNnk)
- [CLASS 6 SANSKRIT (रुचिरा-I) - All chapters - Kailash sharma](https://www.youtube.com/playlist?list=PLeUdn394wLGhs-qfAgnff1naOCOQES6sp)
- [CLASS 7 SANSKRIT (रुचिरा-II) - All chapters - Kailash sharma](https://www.youtube.com/playlist?list=PLeUdn394wLGjfKr-oxwuaBSW5ChSTtXP7)
- [CLASS 9 SANSKRIT (शेमुषी भाग -1) All Chapters - Kailash sharma](https://www.youtube.com/playlist?list=PLeUdn394wLGgZsZYQyKHBbwdX3wGf3xoS)
- [Sanskrit Grammar (संस्कृत व्याकरण)- - Kailash sharma](https://www.youtube.com/playlist?list=PLeUdn394wLGiiKX_yPyTnvanVgbeNBXXS)
- [Class 10 Sanskrit (शेमुषी भाग 2) All Chapters - Kailash sharma ](https://www.youtube.com/playlist?list=PLeUdn394wLGj3e0ixWPMMeK-J68yhRsy2)
- [Manika Class 10 Sanskrit 2024 - Kailash sharma ](https://www.youtube.com/playlist?list=PLeUdn394wLGj_wkLk1a_DCL3mcNU5uyIe)
- [Manika Class 9 Sanskrit 2024 - Kailash sharma ](https://www.youtube.com/playlist?list=PLeUdn394wLGjzk1Bgva2W1x8DeNmVQfze)
- [Class 10 Sanskrit 2024 - Kailash sharma ](https://www.youtube.com/playlist?list=PLeUdn394wLGjV9YC5J048QmhnF2NFZYe1)
- [Class 9 Sanskrit (New Session 2023-24) | Shemushi Book | Complete CBSE Course | All Topics Available - Magnet Brains](https://www.youtube.com/playlist?list=PLVLoWQFkZbhXdJioubzrHkWv9naiARRty)
- [Class 10 Sanskrit Vyakaran (New Session 2023-24) | Vyakaranvithi - Magnet Brains](https://www.youtube.com/playlist?list=PLVLoWQFkZbhUFjVKLqwf52xp3pIXBHCTh)
- [Class 10 Sanskrit Shemushi (New Session 2023-24) | Complete CBSE Course | All Chapters Available - Magnet Brains](https://www.youtube.com/playlist?list=PLVLoWQFkZbhWPMmhpUAAd7wePfISqzKHI)
- [std 8th | sanskrit| marathi medium - shikshan katta](https://www.youtube.com/playlist?list=PLilq6e64k5FPqgvvFj-IAkSZHyRmkI3Ib)
- [संस्कृत क्रियापद व त्यांचे अर्थ - SANSKRIT TEACHER](https://www.youtube.com/playlist?list=PLL7hynOJqNcQ0SA1NJowXDMwaJlRwgQEo)
- [CBSC Sanskrit#english #10th Board_Exam#summery - Vasant Patil](https://www.youtube.com/playlist?list=PLL7hynOJqNcS7Wbnwi80sfvLJKVdwNnzr)
- [Samskrita Shikshanam - Parichaya Exam - Samskrita Bharati - Anuj Valmiki](https://www.youtube.com/playlist?list=PLIhLHnjVhe_nd6fnl5cbwsd4N0GmdKdsr)
- [Pravesha - English G3 - May2022
Anuj Valmiki](https://www.youtube.com/playlist?list=PLIhLHnjVhe_lQyoTu1VZ6hK8y3CLi9AiL)
- [Parichaya - English E1 - Nov2023
Anuj Valmiki](https://www.youtube.com/playlist?list=PLIhLHnjVhe_l3RcIeBgxSmVaUHdXiBJKc)
- [Parichaya - English G2 - May2023
Anuj Valmiki](https://www.youtube.com/playlist?list=PLIhLHnjVhe_l9U87PDbBmpf3ei0gaFKp9)
- [Shiksha - English G2 - Nov2021
Anuj Valmiki](https://www.youtube.com/playlist?list=PLIhLHnjVhe_k4q7Z0qNBeLbG7rlebgjhS)
- [SSC 8th l Sanskrit : Amod l इयत्ता ८ वी : आमोद l Sanskrit Amod with Amit S Nagare](https://www.youtube.com/playlist?list=PLBuQFtY0aaI81z4PgzFX3qI4GbLLed1zE)
- [SSC 9th l Sanskrit : Amod l इयत्ता ९ वी : आमोद l Sanskrit Amod with Amit S Nagare](https://www.youtube.com/playlist?list=PLBuQFtY0aaI-DKVOBiGv14UPrHL7fIDyx)
- [SSC 10th l Sanskrit : Amod l इयत्ता १० वी : आमोद l Sanskrit Amod with Amit S Nagare](https://www.youtube.com/playlist?list=PLBuQFtY0aaI9pXUd7rtFx3txwQKgb1cvo)

## Folks, Channels, Institutes
- [Sanskrit From Home | Vyoma Labs](https://www.sanskritfromhome.org/course-listing.php) Learning Paths, Courses, very comprehensive
- [Dr. Vasudev Prasad](https://www.youtube.com/playlist?list=PLhRKsB88RuSmldpHV7ZfjktP1aGsGBVbF)
- [Sanskrit & Computational Linguistics | Dr Pawan Goyal, IIT Kharagpur](https://www.youtube.com/watch?v=m6IBfoE0hzA)
- [Shaastra Setu - Sanskrit Club IIT Roorkee](https://www.youtube.com/playlist?list=PLjFz5TMhii5rSF0DGqrD-atPq0wMn_O1k)
- [Samsaadhanii Praveshikaa - Sanskrit Club IIT Roorkee](https://www.youtube.com/playlist?list=PLjFz5TMhii5q4Mln6VX_lniW6iDLRNyTm)
- [Sujit Dhekane - Sanskrit Subhashite - Marathi and English Translated](https://www.youtube.com/@sujitdhekane/videos)
- [Central Sanskrit University](https://www.sanskrit.nic.in/)

## Projects
- [Dictionary](http://spokensanskrit.org/)
- [Grammar](https://sanskrit.inria.fr/DICO/grammar.html)
- [Sandhi tool](http://greenmesg.org/sanskrit_online_tools/sanskrit_sandhi_tool.php)
- [UCB Sanskrit tools](https://ubcsanskrit.ca/)
- [Sharada Project](http://sanskrit.jnu.ac.in/sharada/index.jsp)
- [Namami ancient text project](https://www.namami.gov.in/)
- [Rashtriya Sanskrit Sansthan](http://www.sanskrit.nic.in/)
- [Teachers and Institutes for Learning Sanskrit]( https://sanskritdocuments.org/sanskritteachers.html)
- [A Machine Learning project to translate Sanskrit text to English]( http://shivanikohli.me/SanTran/ https://github.com/shivanikohlii/SanTran)
- [Vyomshastra Pathshala](https://sanskritfromhome.in/courses/language/sanskrit)
- [Chinmaya International Foundation]( https://www.chinfo.org/index.php/digital-gallery/video/chinmaya-international-foundation)
- [Digitized SLM Sasnkrit Learning Material?](https://www.sanskrit.nic.in/msp/digitized_slm.php)
- [Vedavaapi](https://www.vedavaapi.org/vedic-knowledge-systems/)


### Indian Knowledge System
- [Learn Sharada Lipi | Learn Sanskrit Online](https://www.youtube.com/playlist?list=PLmozlYyYE-ETiEDyzg3UYg4pbNz31nCEG)
- [National Seminar on Manuscripts](https://www.youtube.com/playlist?list=PLjFl99f9x7pvwoBi498eUvDVG4Fp5PIZu)
- [Dharohar](https://dharohar.org/en/the-cataloguing-process), [Sangrah](https://sangrah.org/), [Sanjaya Singhal](https://www.securemeters.com/in/council/sanjaya-singhal/)
- [Namami - National Mission for Manuscripts](https://www.namami.gov.in/)
- [Bori](https://bori.ac.in/), [Shrinand Bapat](https://bori.academia.edu/ShreenandBapat)
- [Prof Ravikiran](https://www.iiit.ac.in/people/faculty/ravi.kiran/) AI/ML for text detection IIITH [Intelligent Historical Document Image Analysis (IHDIA)](https://ihdia.iiit.ac.in/)
- [Sai Surasal](https://mitvedicsciences.edu.in/archives/team/dr-sai-ramakrishna-susarla), [VedVaapi](https://www.vedavaapi.org/), MIT-ADT Pune, Knowledge Graph, web platform, [Shastra Maps](https://mitvedicsciences.edu.in/shaastric-modeling-fdp)
- [Pawan Goyal IIT KGP](https://www.iitkgp.ac.in/department/CS/faculty/cs-pawang), [Sanskrit Heritage Site](https://sanskrit.inria.fr/)
- [Shaastra Maps: Enabling Conceptual Exploration of Indic Shaastra Texts](https://www.youtube.com/watch?v=S72Bj7EC--U)
- [Shaastric Modeling Course](https://mitvedicsciences.edu.in/enroll/shaastric-modeling)
- [National Youth Conference on Indian Knowledge Systems at Chinmaya Vishwa Vidyapeeth](https://www.youtube.com/playlist?list=PLbQHD8oHpmE066jXXY7rMSazzwlR4JepN)
- [वैदिक गणितम् - Vasant Patil](https://www.youtube.com/playlist?list=PLL7hynOJqNcTdQ1-P3sxut67hZFANxs4t)