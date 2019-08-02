// Files with special characters in their names will kick up OS errors
// This slug function replaces special characters with boring old hyphens

def easySlug(string, repl="-", directory=False):
    import re
    if directory:
        return re.sub("^\.|\.+$", "", easySlug(string, directory=False))
    else:
        return re.sub("[\\\\/:*?\"<>\|]|\ $", repl, string)
