import untangle
from xml.dom.minidom import parseString


def write_default_configuration(file):
    data = {
        'CONNECTION_STRING': 'mysql+pymysql://rod:tt8uyi_ddP9@localhost/Qontasim_SachaDB'
    }

    contents = parseString("""
        <root>
            <configuration>
                <connection_string>{CONNECTION_STRING}</connection_string>
            </configuration>
        </root>
        """.format(**data))

    with open(file, "w") as f:
        f.write(contents.toxml())


class Configuration:

    def __init__(self, file):

        obj = untangle.parse(file)

        # print(obj.root.configuration.connection_string.cdata)
        self.connection_string = obj.root.configuration.connection_string.cdata