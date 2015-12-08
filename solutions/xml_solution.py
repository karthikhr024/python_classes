import xml.etree.ElementTree as ET

root = ET.parse('files/pom.xml').getroot()

# Variables
plugin_dict = {}
plugin_list = []
base = "{http://maven.apache.org/POM/4.0.0}"

# Find 'build' and 'properties' XML tags in root
build = root.find(base + 'build')
properties = root.find(base + 'properties')

# Find 'pluginManagement' XML tag in 'build'
pluginManagement = build.find(base + 'pluginManagement')

# Find 'plugins' XML tag in 'pluginManagement'
plugins = pluginManagement.find(base + 'plugins')

# Populate plugin_list
plugin_list = list(plugins)

# Loop through plugins (of class ElementTree)
for plugin in plugin_list:

        # Get  plugin information
        artifactId_str = plugin.find(base + 'artifactId').text
        name = artifactId_str.replace('-plugin', '')

        # Not all plugins have a groupId !
        try:
            groupId_str = plugin.find(base + 'groupId').text
        except:
            groupId_str = "N/A"

        # Not all plugins have a version !
        try:
            version_str = plugin.find(base + 'version').text
            version_str = version_str[2:-1] # strip '$', '{', and '}' from version
            version_str = properties.find(base + version_str).text
        except:
            version_str = "N/A"

        # Print plugin information
        print artifactId_str.replace('-plugin', '')
        print "\t" + "groupId: " + groupId_str
        print "\t" + "artifactId: " + artifactId_str
        print "\t" + "version: " + version_str

        # Add plugin to dictionary
        plugin_dict[name] = {'artifactId': artifactId_str,
                             'groupId': groupId_str,
                             'version': version_str
                             }

        # Write dict to file:
        with open('files/pom_maven_plugins_output.xml', 'w') as f:
            for pname, sub in plugin_dict.iteritems():
                f.write(pname + "\n")
                for k, v in sub.iteritems():
                    f.write("\t" + k + ": " + v + "\n")