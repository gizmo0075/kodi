import sys
import xbmcplugin, xbmcgui, xbmcaddon

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

xbmcplugin.setContent(int(sys.argv[1]), 'videos')

# Create a list item
url = 'https://example.com/video.mp4'
li = xbmcgui.ListItem(label='Test Video')
li.setInfo('video', {'title': 'Test Video'})
li.setProperty('IsPlayable', 'true')

# Add item to directory
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
