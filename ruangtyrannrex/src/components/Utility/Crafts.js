import ConeIcon from ""
import MorseIcon from ""

const Crafts = [
    {
        avatar: "CARVAN",
        title: "Carvan",
        subheader: "September 10th, 2020",
        titleMedia: "Cone Volume",
        image: ConeIcon,
        contentSummary: "Calculator to calculate cone's volume",
        origin: "Based on Edabit Python Easy challenge",
        overview: "Calculate cone's volume by providing height and radius of the cone",
        detail: "Formula to calculate is (radius x radius x pi x height) / 3. This app is a specialized calculator. Click on button ConeVolume to use the app",
        future: "Next iteration is to produce cone graphic based on the height and radius given",
        appButton: 'Cone Volume'
    },
    {
        avatar: "COINFLIP",
        title: "Coinflip",
        subheader: "September 09th, 2020",
        titleMedia: "Morse Code",
        image: MorseIcon,
        contentSummary: "Turn your words into Morse code",
        origin: "Based on Edabit Python Hard challenge",
        overview: "Convert words from alphabetical letters to Morse Code",
        detail: "Morse codes combined '.' and '_' to form a letter. This iteration is only capable in translating letter per letter to the Morse codes. Click on 'Encode Morse' button to start the application",
        future: "Next iteration is to produced corresponding sounds based on the translation",
        appButton: "Encode Morse"
    },
]

export default Crafts