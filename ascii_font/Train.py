

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


Train = AsciiFont("$")
# flf2a$ 6 6 12 63 13 0 24511 0


# Author :myflix
# Date   : 2003/11/6 19:07:12
# Version: 1.0
# -------------------------------------------------
# -------------------------------------------------
# This font has been created using JavE's FIGlet font export assistant.
# Have a look at: http://www.jave.de
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Changed 2012-05-21: Update to "!" character by patorjk
Train[" "] = (
"          \n"
"    o O O \n"
"   o      \n"
"  TS__[O] \n"
" {======| \n"
"./o--000' "
)

Train["!"] = (
"    _    \n"
"   | |   \n"
"   |_|   \n"
"  _(_)_  \n"
"_| \"\"\" | \n"
"\"`-0-0-' "
)

Train["\""] = (
"   _ _   \n"
"  ( | )  \n"
"   V V   \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["#"] = (
" _| | |_  \n"
"|_  .  _| \n"
"|_     _| \n"
"  |_|_|   \n"
"_|\"\"\"\"\"|  \n"
"\"`-0-0-'  "
)

Train["$"] = (
"   ||_   \n"
"  (_-<   \n"
"  / _/   \n"
"  _||__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["%"] = (
"  _  __  \n"
" (_)/ /  \n"
"   / /_  \n"
"  /_/(_) \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["&"] = (
"  _      \n"
"/ _|___  \n"
"> _|_ _| \n"
"\\_____|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["'"] = (
"   (\")   \n"
"    \\|   \n"
"         \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["("] = (
"   / /   \n"
"  | |    \n"
"  | |    \n"
"  _\\_\\_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train[")"] = (
"  \\\"\\    \n"
"   | |   \n"
"   | |   \n"
"  /_/__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["*"] = (
"  _/\\_   \n"
"  >  <   \n"
"   \\/    \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["+"] = (
"  _|\"|_  \n"
" |_   _| \n"
"   |_|   \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train[","] = (
"         \n"
"    _    \n"
"   ( )   \n"
"  _|/__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["-"] = (
"         \n"
"   ___   \n"
"  |___|  \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["."] = (
"         \n"
"         \n"
"    _    \n"
"  _(_)_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["/"] = (
"      __ \n"
"     /\"/ \n"
"    / /  \n"
"  _/_/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["0"] = (
"    __   \n"
"   /  \\  \n"
"  | () | \n"
"  _\\__/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["1"] = (
"    _    \n"
"   / |   \n"
"   | |   \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["2"] = (
"   ___   \n"
"  |_  )  \n"
"   / /   \n"
"  /___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["3"] = (
"   ____  \n"
"  |__ /  \n"
"   |_ \\  \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["4"] = (
"  _ _    \n"
" | | |   \n"
" |_  _|  \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["5"] = (
"   ___   \n"
"  | __|  \n"
"  |__ \\  \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["6"] = (
"    __   \n"
"   / /   \n"
"  / _ \\  \n"
"  \\___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["7"] = (
"   ____  \n"
"  |__  | \n"
"    / /  \n"
"  _/_/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["8"] = (
"   ___   \n"
"  ( _ )  \n"
"  / _ \\  \n"
"  \\___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["9"] = (
"   ___   \n"
"  / _ \\  \n"
"  \\_, /  \n"
"  _/_/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train[":"] = (
"    _    \n"
"   (_)   \n"
"    _    \n"
"  _(_)_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train[";"] = (
"   (_)   \n"
"    _    \n"
"   ( )   \n"
"  _|/__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["<"] = (
"    __   \n"
"   / /   \n"
"  < <    \n"
"  _\\_\\_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["="] = (
"   ___   \n"
"  |___|  \n"
"  |___|  \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train[">"] = (
"   __    \n"
"   \\ \\   \n"
"    > >  \n"
"  _/_/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["?"] = (
"   ___   \n"
"  |__ \\  \n"
"    /_/  \n"
"  _(_)_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["@"] = (
" / __ \\  \n"
"/ / _` | \n"
"\\ \\__,_| \n"
" \\____/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["A"] = (
"   ___   \n"
"  /   \\  \n"
"  | - |  \n"
"  |_|_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["B"] = (
"   ___   \n"
"  | _ )  \n"
"  | _ \\  \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["C"] = (
"   ___   \n"
"  / __|  \n"
" | (__   \n"
"  \\___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["D"] = (
"   ___   \n"
"  |   \\  \n"
"  | |) | \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["E"] = (
"   ___   \n"
"  | __|  \n"
"  | _|   \n"
"  |___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["F"] = (
"    ___  \n"
"   | __| \n"
"   | _|  \n"
"  _|_|_  \n"
"_| \"\"\" | \n"
"\"`-0-0-' "
)

Train["G"] = (
"   ___   \n"
"  / __|  \n"
" | (_ |  \n"
"  \\___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["H"] = (
"  _  _   \n"
" | || |  \n"
" | __ |  \n"
" |_||_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["I"] = (
"   ___   \n"
"  |_ _|  \n"
"   | |   \n"
"  |___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["J"] = (
"      _  \n"
"   _ | | \n"
"  | || | \n"
"  _\\__/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["K"] = (
"  _  __  \n"
" | |/ /  \n"
" | ' <   \n"
" |_|\\_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["L"] = (
"   _     \n"
"  | |    \n"
"  | |__  \n"
"  |____| \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["M"] = (
" __  __  \n"
"|  \\/  | \n"
"| |\\/| | \n"
"|_|__|_| \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["N"] = (
"  _  _   \n"
" | \\| |  \n"
" | .` |  \n"
" |_|\\_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["O"] = (
"   ___   \n"
"  / _ \\  \n"
" | (_) | \n"
"  \\___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["P"] = (
"    ___  \n"
"   | _ \\ \n"
"   |  _/ \n"
"  _|_|_  \n"
"_| \"\"\" | \n"
"\"`-0-0-' "
)

Train["Q"] = (
"  ___    \n"
" / _ \\   \n"
"| (_) |  \n"
" \\__\\_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["R"] = (
"   ___   \n"
"  | _ \\  \n"
"  |   /  \n"
"  |_|_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["S"] = (
"   ___   \n"
"  / __|  \n"
"  \\__ \\  \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["T"] = (
"  _____  \n"
" |_   _| \n"
"   | |   \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["U"] = (
"  _   _  \n"
" | | | | \n"
" | |_| | \n"
"  \\___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["V"] = (
" __   __ \n"
" \\ \\ / / \n"
"  \\ V /  \n"
"  _\\_/_  \n"
"_| \"\"\"\"| \n"
"\"`-0-0-' "
)

Train["W"] = (
"__      __\n"
"\\ \\    / /\n"
" \\ \\/\\/ / \n"
"  \\_/\\_/  \n"
"_|\"\"\"\"\"|  \n"
"\"`-0-0-'  "
)

Train["X"] = (
" __  __  \n"
" \\ \\/ /  \n"
"  >  <   \n"
" /_/\\_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["Y"] = (
" __   __ \n"
" \\ \\ / / \n"
"  \\ V /  \n"
"  _|_|_  \n"
"_| \"\"\" | \n"
"\"`-0-0-' "
)

Train["Z"] = (
"   ____  \n"
"  |_  /  \n"
"   / /   \n"
"  /___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["["] = (
"  |\"\"|   \n"
"  | |    \n"
"  | |    \n"
"  |__|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["\\"] = (
" __      \n"
" \\ \\     \n"
"  \\ \\    \n"
"  _\\_\\_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["]"] = (
"  |\"\"|   \n"
"   | |   \n"
"   | |   \n"
"  |__|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["^"] = (
"   /\\    \n"
"  |/\\|   \n"
"         \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["_"] = (
"         \n"
"         \n"
"   ___   \n"
"  |___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["`"] = (
"  (\")    \n"
"   \\|    \n"
"         \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

Train["a"] = (
"         \n"
"  __ _   \n"
" / _` |  \n"
" \\__,_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["b"] = (
"  _      \n"
" | |__   \n"
" | '_ \\  \n"
" |_.__/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["c"] = (
"         \n"
"   __    \n"
"  / _|   \n"
"  \\__|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["d"] = (
"     _   \n"
"  __| |  \n"
" / _` |  \n"
" \\__,_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["e"] = (
"         \n"
"   ___   \n"
"  / -_)  \n"
"  \\___|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["f"] = (
"     __  \n"
"    / _| \n"
"   |  _| \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["g"] = (
"   __ _  \n"
"  / _` | \n"
"  \\__, | \n"
"  |___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["h"] = (
"  _      \n"
" | |_    \n"
" | ' \\   \n"
" |_||_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["i"] = (
"    _    \n"
"   (_)   \n"
"   | |   \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["j"] = (
"    (_)  \n"
"    | |  \n"
"   _/ |  \n"
"  |__/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["k"] = (
"   _     \n"
"  | |__  \n"
"  | / /  \n"
"  |_\\_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["l"] = (
"    _    \n"
"   | |   \n"
"   | |   \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["m"] = (
"         \n"
"  _ __   \n"
" | '  \\  \n"
" |_|_|_| \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["n"] = (
"         \n"
"  _ _    \n"
" | ' \\   \n"
" |_||_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["o"] = (
"         \n"
"   ___   \n"
"  / _ \\  \n"
"  \\___/  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["p"] = (
"   _ __  \n"
"  | '_ \\ \n"
"  | .__/ \n"
"  |_|__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["q"] = (
"  __ _   \n"
" / _` |  \n"
" \\__, |  \n"
"  __|_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["r"] = (
"         \n"
"    _ _  \n"
"   | '_| \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["s"] = (
"         \n"
"   ___   \n"
"  (_-<   \n"
"  /__/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["t"] = (
"   _     \n"
"  | |_   \n"
"  |  _|  \n"
"  _\\__|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["u"] = (
"         \n"
"  _  _   \n"
" | +| |  \n"
"  \\_,_|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["v"] = (
"         \n"
"  __ __  \n"
"  \\ V /  \n"
"  _\\_/_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["w"] = (
"          \n"
" __ __ __ \n"
" \\ V  V / \n"
"  \\_/\\_/  \n"
"_|\"\"\"\"\"|  \n"
"\"`-0-0-'  "
)

Train["x"] = (
"         \n"
"  __ __  \n"
"  \\ \\ /  \n"
"  /_\\_\\  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["y"] = (
"   _  _  \n"
"  | || | \n"
"   \\_, | \n"
"  _|__/  \n"
"_| \"\"\"\"| \n"
"\"`-0-0-' "
)

Train["z"] = (
"         \n"
"    ___  \n"
"   |_ /  \n"
"  _/__|  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["{"] = (
"   /\"/   \n"
" _| |    \n"
"  | |    \n"
"  _\\_\\_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["|"] = (
"   |\"|   \n"
"   | |   \n"
"   | |   \n"
"  _|_|_  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["}"] = (
"  \\\"\\    \n"
"   | |_  \n"
"   | |   \n"
"  /_/__  \n"
"_|\"\"\"\"\"| \n"
"\"`-0-0-' "
)

Train["~"] = (
"   /\\/|  \n"
"  |/\\/   \n"
"         \n"
"  _____  \n"
"_|     | \n"
"\"`-0-0-' "
)

