"""
By default, activitywatch also tracks the window title of the active window. This adapted version of activitywatch disables this. However, from some websites, we want to
track the general category of the website (e.g. news, gaming, shopping, ...) OR the explicit website (only for some social media/chat websites).

The goal of these utility functions is to map the explicit window titles from websites into their general categories (e.g. www.theguardian.com -> News).
And explicitely track some social media/chat websites (e.g. www.facebook.com -> Facebook).

Only for browser applications (e.g. Chrome, Safari, Edge, Firefox, Brave Browser, Opera). Other apps have the window title disabled

The full mapping can be found below. If a website is not in the mapping, the window title will be set to 'excluded'.

-- Coded by Simon Perneel
-- mailto:Simon.Perneel@UGent.be
"""

# --- Mapping of URLs and titles to website categories ---
# News websites are explicitly tracked
url_to_cat_map = dict.fromkeys(['www.vrt.be',
                                'www.hln.be',
                                'www.nieuwsblad.be',
                                'www.hln.be',
                                'www.demorgen.be',
                                'www.standaard.be',
                                'www.mo.be',
                                'www.knack.be',
                                'www.bbc.com',
                                'www.aljazeera.com',
                                'www.theguardian.com',
                                'edition.cnn.com',
                                'www.foxnews.com',
                                'www.humo.be'],
                                'News')

# Some social media apps are tracked
url_to_cat_map.update(dict.fromkeys(['www.facebook.com'],
                                    'Facebook'))
url_to_cat_map.update(dict.fromkeys(['www.instagram.com'],
                                    'Instagram'))
url_to_cat_map.update(dict.fromkeys(['www.twitter.com'],
                                    'Twitter'))
url_to_cat_map.update(dict.fromkeys(['www.tiktok.com'],
                                    'TikTok'))
url_to_cat_map.update(dict.fromkeys(['www.youtube.com'],
                                    'Youtube'))

# Some other social media websites are tracked
url_to_cat_map.update(dict.fromkeys(['www.discord.com',
                                     'www.snapchat.com',
                                     'www.bere.al'],
                                    'Social Media - Other'))

#  Chat apps
url_to_cat_map.update(dict.fromkeys(['www.messenger.com',
                                     'www.web.whatsapp.com'],
                                    'Messaging'))

# Forums and blogs
url_to_cat_map.update(dict.fromkeys(['www.reddit.com',
                                     'www.9gag.com',
                                     'www.tumblr.com',
                                     'www.blogspot.com'],
                                    'Forums & Blogs'))

# Email websites
url_to_cat_map.update(dict.fromkeys(['www.mail.google.com',
                                     'www.outlook.office365.com',
                                     'www.yahoo.com',
                                     'www.webmail.scarlet.be'],
                                    'Email'))

# Videoconferencing websites
url_to_cat_map.update(dict.fromkeys(['www.zoom.us',
                                     'meet.google.com'],
                                    'Videoconferencing'))

# Work and productivity websites
url_to_cat_map.update(dict.fromkeys(['calendar.google.com',
                                     'www.teams.microsoft.com',
                                     'www.docs.google.com',
                                     'www.deepl.com',
                                     'www.translate.google.com',
                                     'www.miro.com/login/'],
                                    'Work & Productivity'))

# Video streaming websites
url_to_cat_map.update(dict.fromkeys(['www.streamz.be',
                                     'www.vtm.be',
                                     'www.primevideo.com',
                                     'yelo.telenet.tv',
                                     'www.proximus.be',
                                     'www.hbomax.com',
                                     'www.vimeo.com',
                                     'www.twitch.tv'],
                                    'Video'))

# Gaming websites
url_to_cat_map.update(dict.fromkeys(['www.littlebigsnake.com',
                                     'www.catanuniverse.com',
                                     'www.prosperousuniverse.com',
                                     'www.nl.forgeofempires.com',
                                     'www.agar.io',
                                     'www.play.isleward.com',
                                     'www.linerider.com',
                                     'www.adarkroom.doublespeakgames.com'],
                                    'Entertainment & Games'))

# Music streaming websites
url_to_cat_map.update(dict.fromkeys(['www.spotify.com',
                                     'www.music.apple.com'],
                                    'Music & Audio'))

# Most popular retail and shopping websites
url_to_cat_map.update(dict.fromkeys(['www.zalando.be',
                                     'www.amazon.nl',
                                     'www.bol.com',
                                     'www.coolblue.be',
                                     'www.collectandgo.be',
                                     'www.delhaize.be',
                                     'www.carrefour.be',
                                     'www.ah.be',
                                     'www.foodbag.be',
                                     'www.hellofresh.be'],
                                    'Shopping'))

# Sometimes, the url of the website is not in the window title, but the website name is. Then we still want to track for these
# Therefore, we do this extra title_to_cat_map
title_to_cat_map = dict.fromkeys(['vrt nws', 'nieuwsblad', 'hln', 'de morgen', 'de standaard', 'de morgen', ' mo.be',
                                  'knack', 'bbc ', 'the guardian', 'al jazeera', ' cnn', 'fox news', 'humo'],
                                 'News')
# Same for the other categories
title_to_cat_map.update(dict.fromkeys(['facebook'],
                                      'Facebook'))
title_to_cat_map.update(dict.fromkeys(['instagram'],
                                      'Instagram'))
title_to_cat_map.update(dict.fromkeys(['youtube'],
                                      'Youtube'))
title_to_cat_map.update(dict.fromkeys(['twitter'],
                                      'Twitter'))
title_to_cat_map.update(dict.fromkeys(['tiktok'],
                                      'TikTok'))
title_to_cat_map.update(dict.fromkeys(['bereal'],
                                      'BeReal'))
title_to_cat_map.update(dict.fromkeys(['discord'],
                                      'Discord'))
title_to_cat_map.update(dict.fromkeys(['snapchat'],
                                      'Snapchat'))
title_to_cat_map.update(dict.fromkeys(['whatsapp', 'messenger'],
                                      'Messaging'))
title_to_cat_map.update(dict.fromkeys(['reddit', '9gag', 'tumblr', 'blogspot'],
                                      'Forums & Blogs'))
title_to_cat_map.update(dict.fromkeys(['outlook', 'gmail', 'yahoo', 'scarlet'],
                                      'Email'))
title_to_cat_map.update(dict.fromkeys(['zoom', 'google meet', 'google agenda', 'microsoft teams', 'google documenten',
                                       'google spreadsheets', 'google presentaties', 'google formulieren', 'deepl',
                                       'google translate', 'google drive', 'miro', 'adobe'],
                                      'Work & Productivity'))
title_to_cat_map.update(dict.fromkeys(["netflix", "streamz", "vtm", "prime video", "telenet tv", "proximus pickx", "hbo max", "vimeo", "twitch"],
                                      'Video'))
title_to_cat_map.update(dict.fromkeys(["zalando.be", "amazon.com", "amazon.nl", "bol.com", "coolblue", "collect&go", "delhaize", "carrefour", "albert heijn", "foodbag", "hellofresh"],
                                      'Shopping'))
title_to_cat_map.update(dict.fromkeys(["little big snake", "catan", "prosperous universe", "forge of empires", "agar.io", "isleward", "line rider", "a firelit room"],
                                      'Entertainment & Games'))

def alter_window_info(active_window: dict) -> dict:
    """
    applies the changes to active window from aw-watcher-window
    returns: active window without title (non-browser-apps)
             or altered window with title mapped to category (browser-apps)
    """
    # get information from active window
    keys = active_window.keys()
    active_app = active_window.get('app')
    active_title = active_window.get('title')
    # Only browser apps have a url
    url = False

    # We only have url available for Chrome-(based) browser and Safari
    if 'url' in keys:
        url = True

    browsers = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Brave Browser', 'Opera', 'brave.exe', 'chrome.exe',
                'msedge.exe', 'firefox.exe']

    # Delete title from non-browser apps (for privacy reasons)
    if active_app not in browsers:
        try:
            active_window.pop('title')
        except KeyError:
            pass

        return active_window

    # Change window title to their respective mapping for browser activity
    else:
        altered_title = _map_title(active_title)
        active_window['title'] = altered_title
        # Remove url information
        if url:
            active_window = active_window.pop('url')

        # Window has been updated
        altered_window = active_window

        return altered_window


def _map_url(url):
    """
    maps url to a custom defined category
    if url not in mapping, return 'excluded'
    """
    if url in url_to_cat_map.keys():
        return url_to_cat_map.get(url)
    else:
        return 'excluded'


def _map_title(title):
    """
    maps title to their broad category as defined in title_to_cat_map
    if title not in mapping, return 'excluded'
    """

    for key in title_to_cat_map:
        if key in title.lower():
            title = title_to_cat_map.get(key)
            return title
            break

    # default when not tracked
    title = 'excluded'

    return title
