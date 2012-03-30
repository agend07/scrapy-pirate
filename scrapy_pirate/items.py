# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapyPirateItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class PirateTorrentItem(Item):
    title = Field()
    category = Field()
    link = Field()
    download_link = Field()
    description = Field()
    seeders = Field()
    leechers = Field()




''' pirate torrent - a row from the table

    <tr>
        <td class="vertTh">
            <center>
                <a href="/browse/200" title="More from this category">Video</a><br />
                (<a href="/browse/205" title="More from this category">TV shows</a>)
            </center>
        </td>
        <td>
            <div class="detName"><a href="/torrent/6661072/Dark.Matters.Twisted.But.True.S01E02.HDTV.XviD-DiVERGE.avi" class="detLink" title="Details for Dark.Matters.Twisted.But.True.S01E02.HDTV.XviD-DiVERGE.avi">Dark.Matters.Twisted.But.True.S01E02.HDTV.XviD-DiVERGE.avi</a></div>
            <a href="http://torrents.thepiratebay.org/6661072/Dark.Matters.Twisted.But.True.S01E02.HDTV.XviD-DiVERGE.avi.6661072.TPB.torrent" title="Download this torrent"><img src="http://static.thepiratebay.org/img/dl.gif" class="dl" alt="Download" /></a><a href="magnet:?xt=urn:btih:7268dea57c778326d53ac0636d151b3e759a0095&dn=Dark.Matters.Twisted.But.True.S01E02.HDTV.XviD-DiVERGE.avi&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.ccc.de%3A80" title="Download this torrent using magnet"><img src="http://static.thepiratebay.org/img/icon-magnet.gif" alt="Magnet link" /></a><img src="http://static.thepiratebay.org/img/icon_image.gif" alt="This torrent has a cover image" title="This torrent has a cover image" /><a href="/user/betadoctor"><img src="http://static.thepiratebay.org/img/trusted.png" alt="Trusted" title="Trusted" style="width:11px;" border=0 /></a><img src="http://static.thepiratebay.org/img/11x11p.png" />
            <font class="detDesc">Uploaded <b>42&nbsp;mins&nbsp;ago</b>, Size 350.69&nbsp;MiB, ULed by <a class="detDesc" href="/user/betadoctor/" title="Browse betadoctor">betadoctor</a></font>
        </td>
        <td align="right">2</td>
        <td align="right">20</td>
    </tr>
'''