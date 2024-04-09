# Icelandic

## Upplýsingar um Lokaskýrslu

### Samsetning Verkefnis

- Leyfilegt er að vinna í hópum af 1-3 manns. Ef verið er 3 saman í hóp þarf að leggja aðeins meira í skýrsluna en tilgreint er, t.d. með auka gröfum, ítarlegri umfjöllun og skoðun á fleiri sjónarhornum. Þetta á hins vegar ekki við um lokaverkefnið sem gildir 30% af lokaeinkunn.
- Ef þið eruð 2 saman, gerið ráð fyrir að skýrslan verði um 4-6 bls með gröfum. Skýrslan ætti að vera hnitmiðuð en þó skýr og vel uppsett. Bæði kóðinn og skýrslan gilda jafnt til einkunnar.

### Takmarkanir

- Notkun á ChatGPT eða öðrum sambærilegum gervigreindarverkfærum, sem og afritun kóða frá internetinu, er stranglega bönnuð. Allt starf skal vera ykkar eigið. Uppgötvun á kóða sem er afritaður eða óleyfileg aðstoð mun leiða til þess að allir í hópnum fái 0 fyrir verkefnið.

### Skilafrestur

- Lokaskiladagur er um helgina í síðustu kennsluviku.

### Verkefnislýsing

1. **Útfærsla á K-means reikniritinu í Python** fyrir tvö gagnasett: MNIST og Fashion MNIST.

   a) **Innlestur Gagna**: Setjið gögnin í möppuna sem þið eruð að nota í VSCode. Notið skipunina `!pwd` í kóðablok til að sjá hvar möppan er.

   b) **K-means Fall**: Útfærið kmeans fall sem tekur inn gögn af lengd N og k. Fallið á að skila np fylki af flokkum, af stærð N x 1, með heiltölum frá 0 til k-1, sem tákna flokkaða hluti hvers gagnapunkts. Útfærið nauðsynleg assign og update föll út frá pseudocode í kafla 3.6.

   - Velja upphafspunkta.
   - Ítra þar til samleitni er náð, samleitni er miðað við max_iterations og ef skiptingin breytist ekki eftir assign skref.
     - Ákvarða bestu skiptingu - assign.
     - Ákvarða nýja miðjupunkta - update.
   - Skila bestu skiptingu.

   c) **Myndritunarfall**: Þróið föll til að birta það sem þið viljið sýna í skýrslunni.

2. **Skýrslan**: Má vera gerð í LaTeX, Word eða Python notebook en þarf að vera skilað sem PDF. Hún á ekki að fylgja sömu skýrsluformi og áður; engar keyrslur á Python kóða eða þess háttar skulu vera innifaldar.

### Uppbygging og Efni Skýrslu

- **Inngangur**: Yfirlit yfir verkefnið.
- **Framkvæmd**: Lýsing á útfærsluferlinu og stutt útskýring á algríminu.
- **Niðurstöður**: Umræða um útkomuna og hvernig til tókst.
- **Kóði**: Innifalið notuðu kóðanum, settur fram á snyrtilegan hátt.

#### Efni til Umr

æðu

- Fjallið um gagnasettin og kmeans reikniritið, tilgang þess og hvers vegna það er notað.
- Kostir og gallar við kmeans.
- Ástæður fyrir því að ekki er alltaf flokkað rétt.
- Voru tilteknar myndir sem flokkuðust verr en aðrar.
- Munur á frammistöðu á milli gagnasettanna, ástæður fyrir slíkum mun eða skorti á honum.

#### Óskað Eftir Gröfum/Töflum

- Histogram (súlurit) yfir dreifingu flokkunar ykkar og svo raunverulega flokkunin.
- Töflu yfir hversu góð þyrpingin ykkar er. Hjálparfall verður gefið til að meta þetta.
