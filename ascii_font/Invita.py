

if not '.' in __name__:
    package_name = '__main__'
else:
    package_name = __name__.rsplit(".", 1)[0]

if package_name == "__main__":
    module_name = 'base'
else:
    module_name = package_name + '.' + 'base'

module = __import__(module_name, fromlist=['.'])
AsciiFont = getattr(module, 'AsciiFont')


Invita = AsciiFont("$")
# flf2a$ 6 4 20 0 2


# invita.flf 06/94 pk6811s@acad.drake.edu
# alas, the computer has better handwriting than I do
Invita[" "] = (
"      \n"
"    $$\n"
"   $$ \n"
"  $$  \n"
" $$   \n"
"$$    "
)

Invita["!"] = (
"    /$$\n"
"  $/$  \n"
"  /    \n"
"$o$    \n"
"       \n"
"       "
)

Invita["\""] = (
"   \n"
"//$\n"
"   \n"
"$  \n"
"   \n"
"   "
)

Invita["#"] = (
"        \n"
" -/--/-$\n"
"-/--/-$ \n"
"        \n"
"        \n"
"        "
)

Invita["$"] = (
"    __/_  \n"
"   ( /  )$\n"
"    \\  $  \n"
"(__/_)$   \n"
"  /       \n"
"          "
)

Invita["%"] = (
"       \n"
"  ()/$$\n"
"   /   \n"
" $/()$ \n"
"       \n"
"       "
)

Invita["&"] = (
"  __ $\n"
" (  )$\n"
" ,\\ $ \n"
"(__\\_ \n"
"    ($\n"
"      "
)

Invita["'"] = (
"    \n"
" / $\n"
"    \n"
"$   \n"
"    \n"
"    "
)

Invita["("] = (
"    $ .-$\n"
"   $ / $ \n"
"  $ / $  \n"
" $ / $   \n"
"$ (__ $  \n"
"         "
)

Invita[")"] = (
"    $-.  $\n"
"    $ / $ \n"
"   $ / $  \n"
"  $ / $   \n"
"$_./ $    \n"
"          "
)

Invita["*"] = (
"      \n"
"      \n"
"$_\\/_$\n"
"$ /\\ $\n"
"      \n"
"      "
)

Invita["+"] = (
"     \n"
" $   \n"
"$_|_$\n"
"$ | $\n"
"     \n"
"     "
)

Invita[","] = (
"   $\n"
"   $\n"
"   $\n"
"$  $\n"
"$/  \n"
"    "
)

Invita["-"] = (
"      \n"
"   $ $\n"
"  __ $\n"
" $  $ \n"
"$  $  \n"
"      "
)

Invita["."] = (
"   $\n"
"    \n"
"    \n"
"$o $\n"
"    \n"
"    "
)

Invita["/"] = (
"    $\n"
" $ /$\n"
"  /  \n"
"$/ $ \n"
"$    \n"
"     "
)

Invita["0"] = (
"    __ $\n"
"  /   )$\n"
" /   / $\n"
"(__ / $ \n"
"        \n"
"        "
)

Invita["1"] = (
"    _ $\n"
"  / / $\n"
"   /  $\n"
"  /  $ \n"
" /     \n"
"       "
)

Invita["2"] = (
"   _  $\n"
"  '  )$\n"
" ,--' $\n"
"/___ $ \n"
"      $\n"
"       "
)

Invita["3"] = (
"   _  $\n"
"  '  )$\n"
"   -( $\n"
"(__ )$ \n"
"       \n"
"       "
)

Invita["4"] = (
" _    $\n"
" /   /$\n"
"/___/_$\n"
"   /  $\n"
"  /    \n"
"       "
)

Invita["5"] = (
"   ___$\n"
"  /   $\n"
" /__  $\n"
"____)$ \n"
"       \n"
"       "
)

Invita["6"] = (
"   $__$\n"
"  /   $\n"
" /__  $\n"
"(__ )$ \n"
"       \n"
"       "
)

Invita["7"] = (
" ___  $\n"
"/   / $\n"
"   /  $\n"
"  /  $ \n"
" /     \n"
"       "
)

Invita["8"] = (
"  ___ $\n"
" (   )$\n"
" .--' $\n"
"(___)$ \n"
"       \n"
"       "
)

Invita["9"] = (
"   __ $\n"
" /   )$\n"
"(__,/ $\n"
"   / $ \n"
"  /    \n"
"       "
)

Invita[":"] = (
"    \n"
"   $\n"
"$'$ \n"
"$'$ \n"
"    \n"
"    "
)

Invita[";"] = (
"     \n"
"     \n"
" $o$ \n"
"$  $ \n"
"$/$  \n"
"     "
)

Invita["<"] = (
"     \n"
"  /$$\n"
"$<$$$\n"
"  \\$$\n"
"     \n"
"     "
)

Invita["="] = (
"   $\n"
"$__$\n"
"$__$\n"
"   $\n"
"    \n"
"    "
)

Invita[">"] = (
"     \n"
" \\   \n"
" $>$$\n"
" /   \n"
"     \n"
"     "
)

Invita["?"] = (
"  ___ $\n"
"(    )$\n"
"   / $ \n"
"  o $  \n"
"       \n"
"       "
)

Invita["@"] = (
"   _  $\n"
" /   )$\n"
"/  () $\n"
"\\____/$\n"
"       \n"
"       "
)

Invita["A"] = (
"   _____ $ \n"
"  (, /  |$ \n"
"    /---|$ \n"
" ) /    |_ \n"
"(_/        \n"
"           "
)

Invita["B"] = (
"   ______ $ \n"
"  (, /    )$\n"
"    /---( $ \n"
" ) / ____)  \n"
"(_/ (       \n"
"            "
)

Invita["C"] = (
" )   ___ $ \n"
"(__/_____)$\n"
"  /      $ \n"
" /         \n"
"(______)$  \n"
"           "
)

Invita["D"] = (
"   ______ $ \n"
"  (, /    )$\n"
"    /    /  \n"
"  _/___ /_  \n"
"(_/___ /    \n"
"            "
)

Invita["E"] = (
"     _____)$\n"
"   /      $ \n"
"   )__  $   \n"
" /          \n"
"(_____)$    \n"
"            "
)

Invita["F"] = (
"   ________)$\n"
"  (, /    $  \n"
"    /___,$   \n"
" ) /   $     \n"
"(_/          \n"
"             "
)

Invita["G"] = (
"     _____)$\n"
"   /      $ \n"
"  /   ___ $ \n"
" /     / )$ \n"
"(____ /  $  \n"
"            "
)

Invita["H"] = (
"   ____  ___)$\n"
"  (, /   / $  \n"
"    /---/$    \n"
" ) /   (__    \n"
"(_/           \n"
"              "
)

Invita["I"] = (
"     _____$\n"
"    (, / $ \n"
"      /$   \n"
"  ___/__   \n"
"(__ / $    \n"
"           "
)

Invita["J"] = (
"      _____$\n"
"     (, / $ \n"
"       /$   \n"
"   ___/__   \n"
" /   / $    \n"
"(__ / $     "
)

Invita["K"] = (
"   __   __)$\n"
"  (, ) / $  \n"
"    /( $    \n"
" ) /  \\_    \n"
"(_/         \n"
"            "
)

Invita["L"] = (
"     _ $  \n"
"$___/__)$ \n"
"(, /  $   \n"
"  /  $    \n"
" (_____$  \n"
"        ) "
)

Invita["M"] = (
"   __     __)$\n"
"  (, /|  /|$  \n"
"    / | / |$  \n"
" ) /  |/  |_  \n"
"(_/   '    $  \n"
"              "
)

Invita["N"] = (
"   __     __)$\n"
"  (, /|  / $  \n"
"    / | / $   \n"
" ) /  |/ $    \n"
"(_/   ' $     \n"
"              "
)

Invita["O"] = (
"     ___ $\n"
"   /(,  )$\n"
"  /    /$ \n"
" /    /$  \n"
"(___ /$   \n"
"          "
)

Invita["P"] = (
"    _____ $ \n"
"   (, /   )$\n"
"    _/__ /$ \n"
"    /    $  \n"
" ) /    $   \n"
"(_/         "
)

Invita["Q"] = (
"    ____ $ \n"
"   (,    )$\n"
"        /$ \n"
"  ____ /$  \n"
"(____ (    \n"
"       )   "
)

Invita["R"] = (
"   _____ $ \n"
"  (, /   )$\n"
"    /__ /$ \n"
" ) /   \\_  \n"
"(_/        \n"
"           "
)

Invita["S"] = (
"      __ $\n"
"  (__/  )$\n"
"    /$    \n"
" ) /$     \n"
"(_/$      \n"
"          "
)

Invita["T"] = (
"    ______)$\n"
"   (, / $   \n"
"     / $    \n"
"$ ) / $     \n"
"$(_/ $      \n"
"            "
)

Invita["U"] = (
" __     __)$\n"
"(, /   / $  \n"
"  /   /$    \n"
" /   /$     \n"
"(___(_      \n"
"            "
)

Invita["V"] = (
" __    __)$\n"
"(, )  / $  \n"
"   | /$    \n"
"   |/$     \n"
"   |$      \n"
"           "
)

Invita["W"] = (
" __       __)$\n"
"(, )  |  / $  \n"
"   | /| /$    \n"
"   |/ |/$     \n"
"   /  |$      \n"
"              "
)

Invita["X"] = (
" __   __)$ \n"
"(,  |/ $   \n"
"    | $    \n"
" ) /|_     \n"
"(_/  $     \n"
"           "
)

Invita["Y"] = (
"  __     __)$\n"
" (, )   / $  \n"
"   /   /$    \n"
"  (___/_     \n"
" )   / $     \n"
"(__ / $      "
)

Invita["Z"] = (
"   ___$  \n"
"  (,   )$\n"
"      /$ \n"
"    _/_  \n"
" )   /   \n"
"(__ /    "
)

Invita["["] = (
"    $ _ $\n"
"   $ / $ \n"
"  $ / $  \n"
" $ / $   \n"
"$ /_ $   \n"
"         "
)

Invita["\\"] = (
"$    \n"
"$\\ $ \n"
"  \\  \n"
" $ \\$\n"
"    $\n"
"     "
)

Invita["]"] = (
"    $ _  $\n"
"    $ / $ \n"
"   $ / $  \n"
"  $ / $   \n"
"$ _/ $    \n"
"          "
)

Invita["^"] = (
"   _  \n"
" $/ \\$\n"
"      \n"
" $   $\n"
"      \n"
"      "
)

Invita["_"] = (
" \n"
" \n"
" \n"
" \n"
"_\n"
" "
)

Invita["`"] = (
"       \n"
"$$$\\$$$\n"
"       \n"
" $   $ \n"
"       \n"
"       "
)

Invita["a"] = (
"    \n"
"    \n"
" _$ \n"
"(_(_\n"
"    \n"
"    "
)

Invita["b"] = (
"     \n"
"  /)$\n"
" (/_ \n"
"/_)$ \n"
"     \n"
"     "
)

Invita["c"] = (
"   \n"
"   \n"
" _$\n"
"(__\n"
"   \n"
"   "
)

Invita["d"] = (
"      \n"
"   /)$\n"
" _(/$ \n"
"(_(_  \n"
"      \n"
"      "
)

Invita["e"] = (
"    \n"
"    \n"
" $_$\n"
"_(/_\n"
"    \n"
"    "
)

Invita["f"] = (
"       \n"
"    /)$\n"
"   //$ \n"
"  /(_  \n"
" /)    \n"
"(/     "
)

Invita["g"] = (
"      \n"
"      \n"
"   _ $\n"
"  (_/_\n"
" .-/  \n"
"(_/   "
)

Invita["h"] = (
"    \n"
" /)$\n"
"(/ $\n"
"/ )_\n"
"    \n"
"    "
)

Invita["i"] = (
"    \n"
"  ,$\n"
"  $ \n"
"_(_ \n"
"    \n"
"    "
)

Invita["j"] = (
"       \n"
"    $,$\n"
"     $ \n"
"   $/_ \n"
" .-/   \n"
"(_/    "
)

Invita["k"] = (
"    \n"
" /)$\n"
"(/_$\n"
"/(__\n"
"    \n"
"    "
)

Invita["l"] = (
"     \n"
"  /)$\n"
" //$ \n"
"(/_  \n"
"     \n"
"     "
)

Invita["m"] = (
"     \n"
"     \n"
"___$ \n"
"// (_\n"
"     \n"
"     "
)

Invita["n"] = (
"    \n"
"    \n"
"__$ \n"
"/ (_\n"
"    \n"
"    "
)

Invita["o"] = (
"    \n"
"    \n"
" ___\n"
"(_) \n"
"    \n"
"    "
)

Invita["p"] = (
"        \n"
"        \n"
"    __ $\n"
"    /_)_\n"
" .-/    \n"
"(_/     "
)

Invita["q"] = (
"    \n"
"    \n"
" _ $\n"
"(_/_\n"
" /( \n"
"(_) "
)

Invita["r"] = (
"    \n"
"    \n"
" __$\n"
"/ (_\n"
"    \n"
"    "
)

Invita["s"] = (
"    \n"
"    \n"
"$_ $\n"
"/_)_\n"
"    \n"
"    "
)

Invita["t"] = (
"    \n"
"    \n"
"_/_ \n"
"(__ \n"
"    \n"
"    "
)

Invita["u"] = (
"    \n"
"    \n"
"   $\n"
"(_(_\n"
"    \n"
"    "
)

Invita["v"] = (
"    \n"
"    \n"
"_ _ \n"
"(/__\n"
"    \n"
"    "
)

Invita["w"] = (
"     \n"
"     \n"
"_   _\n"
"(_(/$\n"
"     \n"
"     "
)

Invita["x"] = (
"     \n"
"     \n"
"__/$$\n"
"$/(__\n"
"/    \n"
"     "
)

Invita["y"] = (
"      \n"
"      \n"
"  $  $\n"
"  (_/_\n"
" .-/  \n"
"(_/   "
)

Invita["z"] = (
"      \n"
"      \n"
"   _ $\n"
"  '_)_\n"
" .-/  \n"
"(_/   "
)

Invita["{"] = (
"    $ .-$\n"
"   $ / $ \n"
" $ -  $  \n"
" $ / $   \n"
"$ (__ $  \n"
"         "
)

Invita["|"] = (
"  $   $\n"
"  $ | $\n"
"  $ | $\n"
"  $ | $\n"
"       \n"
"       "
)

Invita["}"] = (
"    $-.  $\n"
"    $ / $ \n"
"   $  - $ \n"
"  $ / $   \n"
"$_./ $    \n"
"          "
)

Invita["~"] = (
"  _   _$\n"
"$' `-'  \n"
"        \n"
"$     $ \n"
"        \n"
"        "
)

