

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


Big = AsciiFont("$")
# flf2a$ 8 6 59 15 10 0 24463


# Big by Glenn Chappell 4/93 -- based on Standard
# Includes ISO Latin-1
# Greek characters by Bruce Jakeway <pbjakeway@neumann.uwaterloo.ca>
# figlet release 2.2 -- November 1996
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.
Big[" "] = (
" $\n"
" $\n"
" $\n"
" $\n"
" $\n"
" $\n"
" $\n"
" $"
)

Big["!"] = (
"  _ \n"
" | |\n"
" | |\n"
" | |\n"
" |_|\n"
" (_)\n"
"    \n"
"    "
)

Big["\""] = (
"  _ _ \n"
" ( | )\n"
"  V V \n"
"   $  \n"
"   $  \n"
"   $  \n"
"      \n"
"      "
)

Big["#"] = (
"    _  _   \n"
"  _| || |_ \n"
" |_  __  _|\n"
"  _| || |_ \n"
" |_  __  _|\n"
"   |_||_|  \n"
"           \n"
"           "
)

Big["$"] = (
"   _  \n"
"  | | \n"
" / __)\n"
" \\__ \\\n"
" (   /\n"
"  |_| \n"
"      \n"
"      "
)

Big["%"] = (
"  _   __\n"
" (_) / /\n"
"    / / \n"
"   / /  \n"
"  / / _ \n"
" /_/ (_)\n"
"        \n"
"        "
)

Big["&"] = (
"         \n"
"   ___   \n"
"  ( _ )  \n"
"  / _ \\/\\\n"
" | (_>  <\n"
"  \\___/\\/\n"
"         \n"
"         "
)

Big["'"] = (
"  _ \n"
" ( )\n"
" |/ \n"
"  $ \n"
"  $ \n"
"  $ \n"
"    \n"
"    "
)

Big["("] = (
"   __\n"
"  / /\n"
" | | \n"
" | | \n"
" | | \n"
" | | \n"
"  \\_\\\n"
"     "
)

Big[")"] = (
" __  \n"
" \\ \\ \n"
"  | |\n"
"  | |\n"
"  | |\n"
"  | |\n"
" /_/ \n"
"     "
)

Big["*"] = (
"     _    \n"
"  /\\| |/\\ \n"
"  \\ ` ' / \n"
" |_     _|\n"
"  / , . \\ \n"
"  \\/|_|\\/ \n"
"          \n"
"          "
)

Big["+"] = (
"        \n"
"    _   \n"
"  _| |_ \n"
" |_   _|\n"
"   |_|  \n"
"    $   \n"
"        \n"
"        "
)

Big[","] = (
"    \n"
"    \n"
"    \n"
"    \n"
"  _ \n"
" ( )\n"
" |/ \n"
"    "
)

Big["-"] = (
"         \n"
"         \n"
"  ______ \n"
" |______|\n"
"     $   \n"
"     $   \n"
"         \n"
"         "
)

Big["."] = (
"    \n"
"    \n"
"    \n"
"    \n"
"  _ \n"
" (_)\n"
"    \n"
"    "
)

Big["/"] = (
"      __\n"
"     / /\n"
"    / / \n"
"   / /  \n"
"  / /   \n"
" /_/    \n"
"        \n"
"        "
)

Big["0"] = (
"   ___  \n"
"  / _ \\ \n"
" | | | |\n"
" | | | |\n"
" | |_| |\n"
"  \\___/ \n"
"        \n"
"        "
)

Big["1"] = (
"  __ \n"
" /_ |\n"
"  | |\n"
"  | |\n"
"  | |\n"
"  |_|\n"
"     \n"
"     "
)

Big["2"] = (
"  ___  \n"
" |__ \\ \n"
"   $) |\n"
"   / / \n"
"  / /_ \n"
" |____|\n"
"       \n"
"       "
)

Big["3"] = (
"  ____  \n"
" |___ \\ \n"
"   __) |\n"
"  |__ < \n"
"  ___) |\n"
" |____/ \n"
"        \n"
"        "
)

Big["4"] = (
"  _  _   \n"
" | || |  \n"
" | || |_ \n"
" |__   _|\n"
"    | |  \n"
"    |_|  \n"
"         \n"
"         "
)

Big["5"] = (
"  _____ \n"
" | ____|\n"
" | |__  \n"
" |___ \\ \n"
"  ___) |\n"
" |____/ \n"
"        \n"
"        "
)

Big["6"] = (
"    __  \n"
"   / /  \n"
"  / /_  \n"
" | '_ \\ \n"
" | (_) |\n"
"  \\___/ \n"
"        \n"
"        "
)

Big["7"] = (
"  ______ \n"
" |____  |\n"
"    $/ / \n"
"    / /  \n"
"   / /   \n"
"  /_/    \n"
"         \n"
"         "
)

Big["8"] = (
"   ___  \n"
"  / _ \\ \n"
" | (_) |\n"
"  > _ < \n"
" | (_) |\n"
"  \\___/ \n"
"        \n"
"        "
)

Big["9"] = (
"   ___  \n"
"  / _ \\ \n"
" | (_) |\n"
"  \\__, |\n"
"    / / \n"
"   /_/  \n"
"        \n"
"        "
)

Big[":"] = (
"    \n"
"  _ \n"
" (_)\n"
"  $ \n"
"  _ \n"
" (_)\n"
"    \n"
"    "
)

Big[";"] = (
"    \n"
"  _ \n"
" (_)\n"
"  $ \n"
"  _ \n"
" ( )\n"
" |/ \n"
"    "
)

Big["<"] = (
"    __\n"
"   / /\n"
"  / / \n"
" < <  \n"
"  \\ \\ \n"
"   \\_\\\n"
"      \n"
"      "
)

Big["="] = (
"         \n"
"  ______ \n"
" |______|\n"
"  ______ \n"
" |______|\n"
"         \n"
"         \n"
"         "
)

Big[">"] = (
" __   \n"
" \\ \\  \n"
"  \\ \\ \n"
"   > >\n"
"  / / \n"
" /_/  \n"
"      \n"
"      "
)

Big["?"] = (
"  ___  \n"
" |__ \\ \n"
"    ) |\n"
"   / / \n"
"  |_|  \n"
"  (_)  \n"
"       \n"
"       "
)

Big["@"] = (
"          \n"
"    ____  \n"
"   / __ \\ \n"
"  / / _` |\n"
" | | (_| |\n"
"  \\ \\__,_|\n"
"   \\____/ \n"
"          "
)

Big["A"] = (
"           \n"
"     /\\    \n"
"    /  \\   \n"
"   / /\\ \\  \n"
"  / ____ \\ \n"
" /_/    \\_\\\n"
"           \n"
"           "
)

Big["B"] = (
"  ____  \n"
" |  _ \\ \n"
" | |_) |\n"
" |  _ < \n"
" | |_) |\n"
" |____/ \n"
"        \n"
"        "
)

Big["C"] = (
"   _____ \n"
"  / ____|\n"
" | | $   \n"
" | | $   \n"
" | |____ \n"
"  \\_____|\n"
"         \n"
"         "
)

Big["D"] = (
"  _____  \n"
" |  __ \\ \n"
" | |  | |\n"
" | |  | |\n"
" | |__| |\n"
" |_____/ \n"
"         \n"
"         "
)

Big["E"] = (
"  ______ \n"
" |  ____|\n"
" | |__   \n"
" |  __|  \n"
" | |____ \n"
" |______|\n"
"         \n"
"         "
)

Big["F"] = (
"  ______ \n"
" |  ____|\n"
" | |__   \n"
" |  __|  \n"
" | |     \n"
" |_|     \n"
"         \n"
"         "
)

Big["G"] = (
"   _____ \n"
"  / ____|\n"
" | |  __ \n"
" | | |_ |\n"
" | |__| |\n"
"  \\_____|\n"
"         \n"
"         "
)

Big["H"] = (
"  _    _ \n"
" | |  | |\n"
" | |__| |\n"
" |  __  |\n"
" | |  | |\n"
" |_|  |_|\n"
"         \n"
"         "
)

Big["I"] = (
"  _____ \n"
" |_   _|\n"
"   | |  \n"
"   | |  \n"
"  _| |_ \n"
" |_____|\n"
"        \n"
"        "
)

Big["J"] = (
"       _ \n"
"      | |\n"
"      | |\n"
"  _   | |\n"
" | |__| |\n"
"  \\____/ \n"
"         \n"
"         "
)

Big["K"] = (
"  _  __\n"
" | |/ /\n"
" | ' / \n"
" |  <  \n"
" | . \\ \n"
" |_|\\_\\\n"
"       \n"
"       "
)

Big["L"] = (
"  _      \n"
" | |     \n"
" | |     \n"
" | |     \n"
" | |____ \n"
" |______|\n"
"         \n"
"         "
)

Big["M"] = (
"  __  __ \n"
" |  \\/  |\n"
" | \\  / |\n"
" | |\\/| |\n"
" | |  | |\n"
" |_|  |_|\n"
"         \n"
"         "
)

Big["N"] = (
"  _   _ \n"
" | \\ | |\n"
" |  \\| |\n"
" | . ` |\n"
" | |\\  |\n"
" |_| \\_|\n"
"        \n"
"        "
)

Big["O"] = (
"   ____  \n"
"  / __ \\ \n"
" | |  | |\n"
" | |  | |\n"
" | |__| |\n"
"  \\____/ \n"
"         \n"
"         "
)

Big["P"] = (
"  _____  \n"
" |  __ \\ \n"
" | |__) |\n"
" |  ___/ \n"
" | |     \n"
" |_|     \n"
"         \n"
"         "
)

Big["Q"] = (
"   ____  \n"
"  / __ \\ \n"
" | |  | |\n"
" | |  | |\n"
" | |__| |\n"
"  \\___\\_\\\n"
"         \n"
"         "
)

Big["R"] = (
"  _____  \n"
" |  __ \\ \n"
" | |__) |\n"
" |  _  / \n"
" | | \\ \\ \n"
" |_|  \\_\\\n"
"         \n"
"         "
)

Big["S"] = (
"   _____ \n"
"  / ____|\n"
" | (___  \n"
"  \\___ \\ \n"
"  ____) |\n"
" |_____/ \n"
"         \n"
"         "
)

Big["T"] = (
"  _______ \n"
" |__   __|\n"
"    | |   \n"
"    | |   \n"
"    | |   \n"
"    |_|   \n"
"          \n"
"          "
)

Big["U"] = (
"  _    _ \n"
" | |  | |\n"
" | |  | |\n"
" | |  | |\n"
" | |__| |\n"
"  \\____/ \n"
"         \n"
"         "
)

Big["V"] = (
" __      __\n"
" \\ \\    / /\n"
"  \\ \\  / / \n"
"   \\ \\/ /  \n"
"    \\  /   \n"
"     \\/    \n"
"           \n"
"           "
)

Big["W"] = (
" __          __\n"
" \\ \\        / /\n"
"  \\ \\  /\\  / / \n"
"   \\ \\/  \\/ /  \n"
"    \\  /\\  /   \n"
"     \\/  \\/    \n"
"               \n"
"               "
)

Big["X"] = (
" __   __\n"
" \\ \\ / /\n"
"  \\ V / \n"
"   > <  \n"
"  / . \\ \n"
" /_/ \\_\\\n"
"        \n"
"        "
)

Big["Y"] = (
" __     __\n"
" \\ \\   / /\n"
"  \\ \\_/ / \n"
"   \\   /  \n"
"    | |   \n"
"    |_|   \n"
"          \n"
"          "
)

Big["Z"] = (
"  ______\n"
" |___  /\n"
"   $/ / \n"
"   / /  \n"
"  / /__ \n"
" /_____|\n"
"        \n"
"        "
)

Big["["] = (
"  ___ \n"
" |  _|\n"
" | |  \n"
" | |  \n"
" | |  \n"
" | |_ \n"
" |___|\n"
"      "
)

Big["\\"] = (
" __     \n"
" \\ \\    \n"
"  \\ \\   \n"
"   \\ \\  \n"
"    \\ \\ \n"
"     \\_\\\n"
"        \n"
"        "
)

Big["]"] = (
"  ___ \n"
" |_  |\n"
"   | |\n"
"   | |\n"
"   | |\n"
"  _| |\n"
" |___|\n"
"      "
)

Big["^"] = (
"  /\\ \n"
" |/\\|\n"
"   $ \n"
"   $ \n"
"   $ \n"
"   $ \n"
"     \n"
"     "
)

Big["_"] = (
"         \n"
"         \n"
"         \n"
"         \n"
"         \n"
"     $   \n"
"  ______ \n"
" |______|"
)

Big["`"] = (
"  _ \n"
" ( )\n"
"  \\|\n"
"  $ \n"
"  $ \n"
"  $ \n"
"    \n"
"    "
)

Big["a"] = (
"        \n"
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__,_|\n"
"        \n"
"        "
)

Big["b"] = (
"  _     \n"
" | |    \n"
" | |__  \n"
" | '_ \\ \n"
" | |_) |\n"
" |_.__/ \n"
"        \n"
"        "
)

Big["c"] = (
"       \n"
"       \n"
"   ___ \n"
"  / __|\n"
" | (__ \n"
"  \\___|\n"
"       \n"
"       "
)

Big["d"] = (
"      _ \n"
"     | |\n"
"   __| |\n"
"  / _` |\n"
" | (_| |\n"
"  \\__,_|\n"
"        \n"
"        "
)

Big["e"] = (
"       \n"
"       \n"
"   ___ \n"
"  / _ \\\n"
" |  __/\n"
"  \\___|\n"
"       \n"
"       "
)

Big["f"] = (
"   __ \n"
"  / _|\n"
" | |_ \n"
" |  _|\n"
" | |  \n"
" |_|  \n"
"      \n"
"      "
)

Big["g"] = (
"        \n"
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__, |\n"
"   __/ |\n"
"  |___/ "
)

Big["h"] = (
"  _     \n"
" | |    \n"
" | |__  \n"
" | '_ \\ \n"
" | | | |\n"
" |_| |_|\n"
"        \n"
"        "
)

Big["i"] = (
"  _ \n"
" (_)\n"
"  _ \n"
" | |\n"
" | |\n"
" |_|\n"
"    \n"
"    "
)

Big["j"] = (
"    _ \n"
"   (_)\n"
"    _ \n"
"   | |\n"
"   | |\n"
"   | |\n"
"  _/ |\n"
" |__/ "
)

Big["k"] = (
"  _    \n"
" | |   \n"
" | | __\n"
" | |/ /\n"
" |   < \n"
" |_|\\_\\\n"
"       \n"
"       "
)

Big["l"] = (
"  _ \n"
" | |\n"
" | |\n"
" | |\n"
" | |\n"
" |_|\n"
"    \n"
"    "
)

Big["m"] = (
"            \n"
"            \n"
"  _ __ ___  \n"
" | '_ ` _ \\ \n"
" | | | | | |\n"
" |_| |_| |_|\n"
"            \n"
"            "
)

Big["n"] = (
"        \n"
"        \n"
"  _ __  \n"
" | '_ \\ \n"
" | | | |\n"
" |_| |_|\n"
"        \n"
"        "
)

Big["o"] = (
"        \n"
"        \n"
"   ___  \n"
"  / _ \\ \n"
" | (_) |\n"
"  \\___/ \n"
"        \n"
"        "
)

Big["p"] = (
"        \n"
"        \n"
"  _ __  \n"
" | '_ \\ \n"
" | |_) |\n"
" | .__/ \n"
" | |    \n"
" |_|    "
)

Big["q"] = (
"        \n"
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__, |\n"
"     | |\n"
"     |_|"
)

Big["r"] = (
"       \n"
"       \n"
"  _ __ \n"
" | '__|\n"
" | |   \n"
" |_|   \n"
"       \n"
"       "
)

Big["s"] = (
"      \n"
"      \n"
"  ___ \n"
" / __|\n"
" \\__ \\\n"
" |___/\n"
"      \n"
"      "
)

Big["t"] = (
"  _   \n"
" | |  \n"
" | |_ \n"
" | __|\n"
" | |_ \n"
"  \\__|\n"
"      \n"
"      "
)

Big["u"] = (
"        \n"
"        \n"
"  _   _ \n"
" | | | |\n"
" | |_| |\n"
"  \\__,_|\n"
"        \n"
"        "
)

Big["v"] = (
"        \n"
"        \n"
" __   __\n"
" \\ \\ / /\n"
"  \\ V / \n"
"   \\_/  \n"
"        \n"
"        "
)

Big["w"] = (
"           \n"
"           \n"
" __      __\n"
" \\ \\ /\\ / /\n"
"  \\ V  V / \n"
"   \\_/\\_/  \n"
"           \n"
"           "
)

Big["x"] = (
"       \n"
"       \n"
" __  __\n"
" \\ \\/ /\n"
"  >  < \n"
" /_/\\_\\\n"
"       \n"
"       "
)

Big["y"] = (
"        \n"
"        \n"
"  _   _ \n"
" | | | |\n"
" | |_| |\n"
"  \\__, |\n"
"   __/ |\n"
"  |___/ "
)

Big["z"] = (
"      \n"
"      \n"
"  ____\n"
" |_  /\n"
"  / / \n"
" /___|\n"
"      \n"
"      "
)

Big["{"] = (
"    __\n"
"   / /\n"
"  | | \n"
" / /  \n"
" \\ \\  \n"
"  | | \n"
"   \\_\\\n"
"      "
)

Big["|"] = (
"  _ \n"
" | |\n"
" | |\n"
" | |\n"
" | |\n"
" | |\n"
" | |\n"
" |_|"
)

Big["}"] = (
" __   \n"
" \\ \\  \n"
"  | | \n"
"   \\ \\\n"
"   / /\n"
"  | | \n"
" /_/  \n"
"      "
)

Big["~"] = (
"  /\\/|\n"
" |/\\/ \n"
"   $  \n"
"   $  \n"
"   $  \n"
"   $  \n"
"      \n"
"      "
)

