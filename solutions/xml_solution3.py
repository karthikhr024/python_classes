import xml.etree.ElementTree as ET
import re

class Plugin(object):
    """ A plugin has a name, an artifactId, a groupId and a version."""
    def __init__(self, plugin, base):
        self.base = base
        self.__get_plugin_info(plugin)

    def __repr__(self):
        to_print = self.name + "\n" + \
        "\t" + "groupId: " + self.groupId + "\n" + \
        "\t" + "artifactId: " + self.artifactId + "\n" + \
        "\t" + "version: " + self.version
        return to_print

    # PRIVATE
    def __concat(self, list_tags):
        """Small function to concatenate the base with the tag name for a list of names.
        Return a tuple containing the new names."""
        t = tuple()
        for tag in list_tags:
            t += (self.base + tag,)
        return t

    def __get_plugin_info(self, plugin):
        """ Takes a plugin of class ElementTree and populates this Plugin object.
        Fields are: name, artifactId, groupid, version"""
        # Get concatenated names
        names = ['artifactId', 'groupId', 'version']
        aId, gId, v = self.__concat(names)

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

        name_str = aId_str.replace('-plugin','')

        # Populate Plugin object
        self.artifactId = aId_str
        self.groupId = gId_str
        self.version = version_str
        self.name = name_str

class POMPluginExtractor(object):
    """This class serves as extractor of plugins from any POM file."""
    def __init__(self, filepath, base):
        self.filepath = filepath
        self.base = base
        self.plugins = []
        self.__get_root()
        self.__get_plugins()

    def print_plugins(self):
        for p in self.plugins:
            print p

    def save_plugins(self, filepath):
        with open(filepath, 'w') as f:
            for p in self.plugins:
                print >>f, p
                print >>f

        print "Plugins saved to %s" % filepath

    # PRIVATE
    def __get_root(self):
        self.root = ET.parse(self.filepath).getroot()

    def __get_plugins(self):
        plugins_path = self.__build_path(['build', 'pluginManagement', 'plugins'], base=self.base)
        plugins = self.root.find(plugins_path)
        for p in plugins.findall(self.base + 'plugin'):
            self.plugins.append(Plugin(p, self.base))

    def __build_path(self, list_, base = ''):
        path = "."
        for a in list_:
            if base:
                path += "/" + base + a
                continue
            path += "/" + a
        return path

# main function
if __name__ == '__main__':
    inputFile = 'files/pom.xml'
    outputFile = 'files/pom_maven_plugins_output.xml'
    base = "{http://maven.apache.org/POM/4.0.0}"

    analyzer = POMPluginExtractor(inputFile, base)
    analyzer.save_plugins(outputFile)
    analyzer.print_plugins()