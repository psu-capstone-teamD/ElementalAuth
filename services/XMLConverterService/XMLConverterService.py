import xml.etree.ElementTree as ET
import re
from GenerateXML import *


class XMLGenerator:

    def convertEvent(self, bxfXML, uuid, outputPath):
        """
        Create a new live event
        :param bxfXML: BXF file as a string.
        :param uuid: UUID of the currently streaming event.
        :param outputPath: The destination address for the stream.
        :return: XML for a live event.
        """
        bxfXML = re.sub('\\sxmlns="[^"]+"', '', bxfXML, count=1)    # prevents namespaces
        root = (ET.fromstring(bxfXML)).find('.//BxfData/Schedule')
        metadata = self.parseMetadata(root)
        try:
            events = self.nextEvent(self.parseEvents(root), uuid)
        except RuntimeError:
            return "Error, could not find the next events."
        liveXML = generateEvent(metadata, events, outputPath)
        return ET.tostring(liveXML.getroot(), encoding='UTF-8', method='xml')

    def convertEventWithProfile(self, bxfXML, profileID, uuid, outputPath):
        """
        Create a new live event
        :param bxfXML: BXF file as a string.
        :param profileID: Required profile ID.
        :param outputPath: The destination address for the stream.
        :return: XML for a live event.
        """
        bxfXML = re.sub('\\sxmlns="[^"]+"', '', bxfXML, count=1)    # prevents namespaces
        root = (ET.fromstring(bxfXML)).find('.//BxfData/Schedule')
        metadata = self.parseMetadata(root)
        try:
            events = self.nextEvent(self.parseEvents(root), uuid)
        except RuntimeError:
            return "Error, could not find the next events."
        liveXML = generateEventWithProfile(metadata, events, profileID)
        return ET.tostring(liveXML.getroot(), encoding='UTF-8', method='xml')

    def convertSchedule(self, bxfXML, profileID):
        """
        Create a schedule in Live XML from a BXF file. This can be
        used for creating new schedules or updating old ones.
        :param bxfXML: BXF file as a string.
        :param profileID: Required profile ID.
        :return: XML for a schedule.
        """
        bxfXML = re.sub('\\sxmlns="[^"]+"', '', bxfXML, count=1)    # prevents namespaces
        root = (ET.fromstring(bxfXML)).find('.//BxfData/Schedule')
        metadata = self.parseMetadata(root)
        try:
            events = self.nextNevents(None, self.parseEvents(root), None)
        except RuntimeError:
            return "Error, could not find the next events"
        liveXML = generateSchedule(profileID, metadata, events)
        return ET.tostring(liveXML.getroot(), encoding='UTF-8', method='xml')

    def convertUpdate(self, bxfXML, currentVideoUUID):
        """
        Create an updated playlist for a live event. Only includes videos that
        are pending after the currently streaming video.
        :param bxfXML: BXF file as a string.
        :param currentVideoUUID: UUID of the currently streaming video.
        :return: XML for a modified live event playlist.
        """
        bxfXML = re.sub('\\sxmlns="[^"]+"', '', bxfXML, count=1)    # prevents namespaces
        root = (ET.fromstring(bxfXML)).find('.//BxfData/Schedule')
        try:
            events = self.nextNevents(1, self.parseEvents(root), currentVideoUUID)
        except RuntimeError:
            return "Error"
        liveXML = generateUpdate(events)
        return ET.tostring(liveXML.getroot(), encoding='UTF-8', method='xml')

    def convertProfile(self, bxfXML, profileName, outputPath):
        """
        Create a new profile for one event in a BXF playlist. The returned
        XML can be used for creating new profiles or updating old ones.
        :param bxfXML: BXF file as a string.
        :param profileName: Unique name for the profile.
        :param outputPath: The destination address for the stream.
        :return: XML for a live event profile.
        """
        liveXML = generateProfile(profileName, outputPath, "UDP")
        return ET.tostring(liveXML.getroot(), encoding='UTF-8', method='xml')

    def parseMetadata(self, root):
        """
        Extract all necessary metadata about the live event from the BXF file.
        :param root: The root element of the BXF tree.
        :return: A dictionary with a key for each piece of metadata.
        """
        metadata = {}
        metadata["name"] = root.find("./ScheduleName").text
        metadata["startTime"] = root.attrib['ScheduleStart']
        metadata["endTime"] = root.attrib['ScheduleEnd']
        return metadata

    def parseEvents(self, root):
        """
        Extract all events from the BXF file.
        :param root: The root element of the BXF tree.
        :return: A list of all video inputs. Each input is a dictionary that includes
        information about the input, including the UUID, order, URI, and event type.
        """
        events = []
        i = 1
        for xmlevent in root.findall("./ScheduledEvent"):
            event = {}
            event["eventType"] = xmlevent.find("./EventData").attrib.get('eventType')
            event["startMode"] = xmlevent.find("./EventData/StartMode").text
            event["endMode"] = xmlevent.find("./EventData/EndMode").text
            event["uid"] = xmlevent.find("./EventData/EventId/EventId").text
            event["order"] = str(i)
            event["uri"] = xmlevent.find("./Content/Media/MediaLocation/Location/AssetServer/PathName").text
            event["startTime"] = xmlevent.find("./EventData/StartDateTime/SmpteDateTime/SmpteTimeCode").text
            event["duration"] = xmlevent.find("./EventData/LengthOption/Duration/SmpteDuration/SmpteTimeCode").text
            event["endTime"] = event["startTime"] + event["duration"]
            events.append(event)
            i += 1
        return events

    def nextEvent(self, events, currentVideoUUID):
        """
        Exclude all inputs except the subsequent n after the currently streaming video.
        :param events: List of all inputs in the BXF file.
        :param currentVideoUUID: UUID of the currently streaming video.
        :return: A list of the next n events or fewer.
        """
        if not currentVideoUUID:
            return [events[0]]
        for i in range(len(events)):
            if events[i]["uid"] == currentVideoUUID:
                if events[i+1]:
                    return [events[i+1]]
        return []

    def nextNevents(self, n, events, currentVideoUUID):
        """
        Exclude all inputs except the subsequent n after the currently streaming video.
        :param n: Number of inputs to include in the live XML. If this value is None,
               all events are returned.
        :param events: List of all inputs in the BXF file.
        :param currentVideoUUID: UUID of the currently streaming video.
        :return: A list of the next n events or fewer.
        """
        if not n:
            return events
        for i in range(len(events)):
            if events[i]["uid"] == currentVideoUUID:
                return [events[i + j] for j in range(1, n + 1) if (i + j) < len(events)]
        return []

    def writetofile(self, liveXML, name):
        ET.ElementTree.write(liveXML, name, encoding='utf-8', xml_declaration=True)

    def elementsEqual(self, e1, e2):
        if e1.tag != e2.tag: return False
        if e1.text != e2.text: return False
        if e1.attrib != e2.attrib: return False
        return all(self.elementsEqual(c1, c2) for c1, c2 in zip(e1, e2))

    def validateXML(self, bxf_xml):
        try:
            ET.fromstring(bxf_xml)
        except ET.ParseError:
            return "StatusCode: 400: Not valid .xml structure"
        return "StatusCode: 200"