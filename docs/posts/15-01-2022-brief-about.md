---
layout : post
title: "Literature"
date : 2022-08-11
categories : Introduction
permalink : /literature/

---

<span style="color:green"> **Following:** </span>\
*Musashi* by Eiji Yoshikawa.

<span style="color:green"> **Most recent read:** </span>
- *Norweigean Wood* by Haruki Murakami.
- <s>Kafka on the Shore by Haruki Murakami.</s>

<span style="color:green"> **Top 3 most surprising reads:** </span>
- *The Lord God Made Them All: All Creatures Great and Small Book 4* by James Herriot.
- *অগ্নিরথ* by Samaresh Majumdar.
- *আরণ্যক* by Bibhutibhushan Bandyopadhyay.

<span style="color:green"> **Personal top 3 popular science reads:** </span>
- *One, Two, Three...Infinity* by George Gamow.
- *The Grand Design* by Stephen Hawking.
- *Cosmos* by Carl Sagan.

<span style="color:green"> **Personal top 3 thrilling scientific books:** </span>
- *A Treatise on Heat* by Meghnad Saha and B. N. Srivastava.
- *Thermodynamics* by Enrico Fermi.
- *Sneaking a Look at God's Cards: Unraveling the Mysteries of Quantum Mechanics* by Giancarlo Ghirardi.

---

**গবেষণা মত্ত চিত্তে আকাশবাণী**

<p>
</p>
<p>
</p>
<span style="color:red"> **Preface:** </span> The creation of this one would be quite technical so just hold on! Almost 4-5 months ago I was really indulged in the concept of Barren Plateaus (অনুরবর মালভূমি). Simulteneously I was engrossed in studying and implementing the [**variational quantum state diagonalization algorithm**](https://www.nature.com/articles/s41534-019-0167-6). To understand the অনুরবর মালভূমি I walked back to 2018 and started studying a very interesting paper titled [**Barren plateaus in quantum neural network training
landscapes**](https://www.nature.com/articles/s41467-018-07090-4?ref=https://githubhelp.com). The things I learned from the paper are: (1) For large class of random quantum circuits (RQC), the average of the gradient of objective accumulates accross zero value, so the probability that the RQC will deviate from average by a small scalar is exponentially small with increasing dimension of system. This is also evident from [**Levy's lemma (not the Levi from AOT)**](https://bookstore.ams.org/surv-89-s). So random walks will have an exponentially small probability of going out of barren plateau. (2) When we construct an [**ansatz**](https://medium.com/arnaldo-gunzi-quantum/what-is-ansatz-31e682b0518b) of L [**quantum logic gates**](https://en.wikipedia.org/wiki/Quantum_logic_gate) we generally have part of it parametrized and other part independent of parameter. The quantum gradient of an [**objective function**](https://en.wikipedia.org/wiki/Mathematical_optimization) (simple example is: energy for VQE) can then be expressed as a commutation of an Hermitian operator (simple example is: Hamiltonian for VQE) and the back (ansatz for 0 to k-1 operations) and forward (ansatz from k-1 to L operations) propagators of the ansatz. Now if either the back or forward proparator forms a 2-design (unlike a 1-design which provides correct value of average the 2-design gives us correct variance, leading to calculate variance of gradient to check barren plateaus) then we see an exponential decay, indicating অনুরবর মালভূমি!
<p>
</p>
Through the poem I express my awe and excitement of finding the appearance of অনুরবর মালভূমি for a toughter problem i.e. quantum state (কুয়ান্তুম দশা) diagonalization algorithm (তির্যককরন গানিতিক পরিভাষ)! <span style="color:green"> **Here goes my journey and the finding** </span>:
<p>
</p>
<p>
</p>
<p>
</p>
<p>অগনিত সময় ধরে ঘেঁটে গবেষণাপত্র,<br>
আসে মস্তিকে নতুন চিন্তার বানী,<br>
বলতে চলেছি এরুপ একটি অভিজ্ঞতার কথা,<br>
এই পদ্যরুপি অভিব্যক্তি তারই কাহিনী।
</p>

<p>
</p>

<p>দিনটা ছিল শনিবার,<br>
বসেছিলাম নিয়ে সদ্য প্রকাশিত একটি পত্র আবার,<br>
তাতেছিল অনুরবর মালভূমির গাঁথা,<br>
পড়িতে চকিতে বিদ্যুৎ আলোতে ভরে গেল আমার মাথা,
</p>

<p>
ভাবলাম আমি চোখ বন্দ করে,<br>
তির্যককরন গানিতিক পরিভাষে কী অনুরবর মালভূমি আছে ভরে?<br>
তত্ত আমার সঠিক প্রমান করিবারে,<br>
আরও একবার শরণাপন্ন হলাম পাইথন কোডের দুয়ারে,<br>
</p>

<p>
</p>

<p>অতীতে লেখা কিছু গাণিতিক পরিভাষ,<br>
আমায় দিয়েছিল কয়েকসারি কোডের আভাস,<br>
সেই নতুন সারি কোডের শ্রমের ফলে,<br>
ভাসলাম আমি এলোমেলো কিছু বর্তনীর ঢলে।
</p>

<p>
</p>

<p>বর্তনীসারির মধ্যদিয়ে করল রাস্তা,<br>
ভিন্ন শ্রেণির মাত্রাযুক্ত কুয়ান্তুম দশা,<br>
বলতে যদি চাই আমি বর্তনী নির্মাণের খেলা,<br>
সব সংযুক্ত একক ও যুগ্ম দ্বারের বসেছিল মেলা।
</p>

<p>
</p>

<p>বিবৃত এই গাণিতিক পরিভাষের গঠন,<br>
ফিরিয়াছিল অবশেষে নতিমাত্রার ভিন্নতার অনুবেদন,<br>
অঙ্কিত পটভূমির শুরু করলাম বিশ্লেষন।
</p>

<p>
</p>

<p>যেখানে এক্স অক্ষ প্রকাশ করে,<br>
ভিন্নশ্রেণীর মাত্রার তথ্য,<br>
সেখানে ওয়াই অক্ষ হুংকার দেয়,<br>
নতিমাত্রার ভিন্নতার কথ্য।
</p>

<p>
</p>

<p>অনুসন্ধানের অবশেষে দেখলাম চোখ মেলে,<br>
ভিন্নশ্রেণীর মাত্রার সাথে নতিমাত্রার ভিন্নতার সূচকীয় হ্রাসের লীলা।
</p>

----
----
**THE FALLEN CASTLE**

<p>
</p>
<p>
</p>
<span style="color:red"> **Preface:** </span> The fallen castle is based on a conversation between me and [**The City Walls of Warsaw old town**](https://en.wikipedia.org/wiki/City_walls_of_Warsaw). It was born in the summer of 2022 at around 2 AM. I just dealt with my (probably) 5th beer. The gentle breeze coming from the beautiful Vistula was without any permission touching my vibrating skin. It was this eternal temporary comfort that moved my legs and made me sit on one of the not-so-high city walls. My eyes were directed towards a shallow valley, whose two sides were surrounded by the concrete of the walls. There was a door at the end of the valley. Completely dark, and melancholy. I felt like the wall, the dungeon like entrance were trying to communicate with me. So without any further ado I grab my mobile, open Keep Notes (someday someone will probably realize it is a museum) and <span style="color:green"> **noted the following extraction of the irreversible, nonrepeatable conversation** </span>:
<p>
</p>
<p>
</p>

<p>The concrete of the castle turns more alive as time heads towards midnight.<br>
Dungeons of the leftovers, thriving for half lifeless beings.
</p>

<p>Throughout history, you saw countless destruction followed by creation,<br>
probably this is the reason behind your and these beings' emotional connection.
</p>

<p>In a future where most of them are unaware of the history,<br>
they stumped your suffering and glory,<br>
to find temporal fun out of knowledge,<br>
which they gained from experiencing your existence.
</p>

<p>
If you could express your feelings what would be your emotions in this instance?
</p>

<p>
I wonder without a clue,<br>
a fruitless search for something in the endless blue.
</p>

<p>
Just the moment before I am about to give in,<br>
I saw a way to interact with you, that is an empty brick plane,<br>
not sure of the fact that how old it could be,<br>
I rest my back on you,<br>
the dungeon like door in front is the only view.
</p>

<p>
Resting my body on you gently,<br>
I felt permission to theorize your inexpressible feeling doubtlessly,<br>
the first thought I had in my mind,<br>
how could you be this kind,<br>
that you are allowing them to obliterate your unfathomable potential,<br>
taking all the negligence without a protest.
</p>

<p>
I wish they knew, the concrete of the castle turning more alive as time heading towards midnight.
</p>

<p>
</p>

<p>
</p>

----
**শিরোনামহীন**
<p>
</p>
<p>
</p>
<span style="color:red"> **Preface:** </span> A week ago (today is 24.10.22) I was watching the Bengali movie [**Stree (1972)**](https://en.wikipedia.org/wiki/Stree_(1972_film)) where Sitapati (সীতাপতি), a homeless youth, comes to landlord Madhav Dutta's house and gets a job as his cameraman. Sitapati with respect mentions Madhav Dutta as king (রাজা). Now our রাজা is very moody. He loves to drink and spend his money. He often arranges late night parties with friends, where he hires expensive dancers, who dances under his huge expensive chandelier (ঝাড়বাতি). In the movie the song "Hazar Takar Jharbatita (হাজার টাকার ঝাড়বাতিটা)" captures a converation between fully drunk রাজা and a rational সীতাপতি who is concerned about রাজা's uncontrolled expances and the way he wastes his money. This is eventually taking him (রাজা) towards a condition where he will face an astounding million of ruppees of debt. The pearl like words of the song were written by great lyricist গৌরিপ্রসন্ন মজুমদার and the cheerful yet sarcastic voice of রাজা was perfectly potrayed by the legend মান্না দে! And equally the rational yet emotional voice of সীতাপতি was captured by another legend হেমন্ত মুখোপাধ্যায়! While listening to the song multiple times I had this thought, "What would সীতাপতি respond to রাজা, who is carelessly flaunting his chandelier's price and his carelessness towards his debt, just to have fun for the night; if I were the writer?" And I figured out I would make সীতাপতি more direct and agreesive, who is rebeling রাজা's irresponsible behavior. I also theorized a response to সীতাপতি if I were রাজা, which also turned out to be more agreesive and direct that would surely hurt me if I were সীতাপতি. So in a nutshell on the way of inventing the non-trivial sequence of words I can doubtlessly say I was in a superposition of রাজা and সীতাপতি's mind state. <span style="color:green"> **Here goes the response** </span>:
<p>
</p>
<p>
</p>
(অপরিবর্তিত)
<p>
</p>
হাজার টাকার ঝাড়বাতিটা,<br>
রাতটাকে যে দিন করেছে,<br>
তারি নীচে বাঈজী নাচে,<br>
ঠুংরি গানের টুকরো ছুঁড়ে,<br>
হাজার টাকার ঝাড়বাতিটা,<br>
তবলচিটা দিচ্ছে ঠেকা,<br>
সারঙ্গীটা সুর ধরেছে,<br>
পিচকিরিটা ঢালছে আতর,<br>
ধূপের ধোঁয়া যাচ্ছে উড়ে,<br>
হাজার টাকার ঝাড়বাতিটা,<br>
পরোয়া তো নেই দু-দশ লাখ,<br>
হয় যদি হোক দেনা,<br>
একটি রাতের মেজাজটা হোক,<br>
অনেক টাকায় কেনা,<br>
আঙুর ফুলের রঙিন রসে,<br>
পানপেয়ালা ঐ ভরেছে,<br>
স্বপ্নে দু চোখ জড়িয়ে আসুক,<br>
সুরভি আর সুরায় সুরে,<br>
হাজার টাকার ঝাড়বাতিটা,<br>
ধরো না, ধরো না সীতাপতি!,<br>
তারি নীচে বাঈজী নাচে,<br>
ঠুংরি গানের টুকরো ছুঁড়ে,<br>
হাজার টাকার ঝাড়বাতিটা,<br>
<p>
</p>
(অপরিবর্তিত)
<p>
</p>
<p>রাজা!<br> 
<p>
</p>
<p>
যে ঝাড়বাতিটা কিনলে তুমি,<br>
হাজার টাকা দিয়ে;
</p>
<p>
দুশতকে দরদাম করে,<br>
পেলাম বাজারে গিয়ে;
</p>
<p>
এইরকম কত আটশতকের,<br>
যদি না খেতে ধাক্কা;
</p>
<p>
বইতে হতোনা, তোমায় আজিরাতে,<br>
দেনা দু-দশ লাখ টাকা;
</p>
<p>
রাজারুপি এই মেজাজ তোমার,<br>
ক্ষনিকের জন্য ঠায়;
</p>
<p>
তুমি ও তোমার মেজাজ দুইয়েই, <br>
আসল রাজা নয়।
</p>
<p>
</p>
<p>
(রাজা বেজায় এক হাসি দিয়ে!)<br>
সীতাপতি? সীতাপতি মনেরেখ!
</p>
<p>
দরদাম করে দুইশতকে,<br>
নকলও পাওয়া যায়;
</p>
<p>
বুদ্ধিমত্তাই আসল রাজা,<br>
কৃপণতা নয়;
</p>
<p>
তুমি কেন এত অবুঝ,<br>
সেই কথাটাই ভাবি;
</p>
<p>
লাখ খানেকের দেনা না হলে,<br>
ক্যামেরায় কি ওই উঠত ছবি? 
</p>
<p>
</p>
<p>
</p>

**(Easily ignorable details)**

<p>
</p>
<p>
</p>
Apart from my state-of-the-art interest in reading science relalted books, I love to study novels which "connects human soul and soil", mostly books written in my mother tongue Bengali. Once upon a time when I was having a long break in between the transition of school and college life, I tend to finish approximately twelve Bengali novels in month, without compromising with my hunger and sleep.  
Just recently I discovered my love to read and write poems. During this discovery, the great Satyajit Ray's creations and hobbies worked as an inspiration to me.