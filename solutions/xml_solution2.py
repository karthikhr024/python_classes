import xml.etree.ElementTree as ET
import re

def concat(list_tags):
    # Small function to concatenate the base with the tag name for a list of names.
    # Return a tuple containing the new names.
    t = tuple()
    for tag in list_tags:
        t += (base + tag,)
    return t

def build_path(list_, base = ''):
    # Create a path from a list of subpaths.
    # If a base is defined, append the based before each path element.
    path = "."
    for a in list_:
        if base:
            path += "/" + base + a
            continue
        path += "/" + a
    return path

def get_plugin_info(plugin):
    # Get concatenated names
    names = ['artifactId', 'groupId', 'version']
    aId, gId, v = concat(names)

    # Get elements from plugin ET
    artifactId = plugin.find(aId)
    groupId = plugin.find(gId)
    version = plugin.find(v)

    # Set output values

    try:
        aId_str = artifactId.text
    except Exception as e:
        raise(e)

    try:
        gId_str = groupId.text
    except:
        gId_str = "N/A"

    try:
        version_str = version.text # strip '$', '{', and '}' from version.text
        try:
            float(version_str)
            version_str = str(version_str)
        except ValueError:
            version_str = version_str[2:-1]
            version_str = properties.find(base + version_str).text
    except:
        version_str = "N/A"

    # Return plugin information
    name_str = aId_str.replace('-plugin','')
    return (aId_str, gId_str, version_str, name_str)

def format_plugin_info(plugin):
    artifactId, groupId, version, name = get_plugin_info(plugin)
    to_print = name + "\n" + \
    "\t" + "groupId: " + groupId + "\n" + \
    "\t" + "artifactId: " + artifactId + "\n" + \
    "\t" + "version: " + version
    return to_print

def print_plugin(plugin):
    print format_plugin_info(plugin)

def write_plugin_to_file(plugin, filepath):
    to_print = format_plugin_info(plugin)
    with open(filepath, 'a') as f:
        f.write(to_print)
        f.write("\n")

# main function
if __name__ == '__main__':
    root = ET.parse('files/pom.xml').getroot()
    base = "{http://maven.apache.org/POM/4.0.0}"

    # Get plugins Element Tree element
    plugins_path    = build_path(['build', 'pluginManagement', 'plugins'], base=base)
    plugins = root.find(plugins_path)

    # Get plugins info and print plugins
    for p in plugins.findall(base + 'plugin'):
        print_plugin(p)
        write_plugin_to_file(p, 'files/pom_maven_plugins_output.xml')