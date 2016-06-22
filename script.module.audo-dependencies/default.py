# Detect machine architecture and prepare execution environment
import os
import xbmc
import xbmcaddon
import xbmcvfs

__addon__             = xbmcaddon.Addon(id='script.module.audo-dependencies')
__dependencies__      = xbmc.translatePath(__addon__.getAddonInfo('path'))

parch                         = os.uname()[4]
pnamemapper                   = xbmc.translatePath(__dependencies__ + '/lib/Cheetah/_namemapper.so')
pobjectify                    = xbmc.translatePath(__dependencies__ + '/lib/lxml/objectify.so')
petree                        = xbmc.translatePath(__dependencies__ + '/lib/lxml/etree.so')
pssl                          = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/SSL.so')
prand                         = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/rand.so')
pcrypto                       = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/crypto.so')
plibcrypto                    = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/libcrypto.so.1.0.0')
plibssl                       = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/libssl.so.1.0.0')
plibcryptolk                  = xbmc.translatePath(__dependencies__ + '/lib/libcrypto.so.1.0.0')
plibssllk                     = xbmc.translatePath(__dependencies__ + '/lib/libssl.so.1.0.0')
pyenc                         = xbmc.translatePath(__dependencies__ + '/lib/_yenc.so')
ppar2                         = xbmc.translatePath(__dependencies__ + '/bin/par2')
punrar                        = xbmc.translatePath(__dependencies__ + '/bin/unrar')
p7za                          = xbmc.translatePath(__dependencies__ + '/bin/7za')

xbmc.log('AUDO: ' + parch + ' architecture detected', level=xbmc.LOGDEBUG)

if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.x86_64')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.x86_64'))
if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.armv6l')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.armv6l'))
if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.armv7l')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.armv7l'))

try:
    if xbmcvfs.exists(pnamemapper):
        xbmcvfs.delete(pnamemapper)
    fnamemapper = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_namemapper.so.' + parch)
    xbmcvfs.copy(fnamemapper, pnamemapper)
    xbmc.log('AUDO: Copied _namemapper.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _namemapper.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pobjectify):
        xbmcvfs.delete(pobjectify)
    fobjectify = xbmc.translatePath(__dependencies__ + '/lib/multiarch/objectify.so.' + parch)
    xbmcvfs.copy(fobjectify, pobjectify)
    xbmc.log('AUDO: Copied objectify.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying objectify.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(petree):
        xbmcvfs.delete(petree)
    fetree = xbmc.translatePath(__dependencies__ + '/lib/multiarch/etree.so.' + parch)
    xbmcvfs.copy(fetree, petree)
    xbmc.log('AUDO: Copied etree.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying etree.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pssl):
        xbmcvfs.delete(pssl)
    fssl = xbmc.translatePath(__dependencies__ + '/lib/multiarch/SSL.so.' + parch)
    xbmcvfs.copy(fssl, pssl)
    xbmc.log('AUDO: Copied SSL.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying SSL.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(prand):
        xbmcvfs.delete(prand)
    frand = xbmc.translatePath(__dependencies__ + '/lib/multiarch/rand.so.' + parch)
    xbmcvfs.copy(frand, prand)
    xbmc.log('AUDO: Copied rand.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying rand.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pcrypto):
        xbmcvfs.delete(pcrypto)
    fcrypto = xbmc.translatePath(__dependencies__ + '/lib/multiarch/crypto.so.' + parch)
    xbmcvfs.copy(fcrypto, pcrypto)
    xbmc.log('AUDO: Copied crypto.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying crypto.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibcrypto):
        xbmcvfs.delete(plibcrypto)
    flibcrypto = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libcrypto.so.1.0.0.' + parch)
    xbmcvfs.copy(flibcrypto, plibcrypto)
    os.symlink(plibcrypto, plibcryptolk)
    xbmc.log('AUDO: Copied libcrypto for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libcrypto for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibssl):
        xbmcvfs.delete(plibssl)
    flibssl = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libssl.so.1.0.0.' + parch)
    xbmcvfs.copy(flibssl, plibssl)
    os.symlink(plibssl, plibssllk)
    xbmc.log('AUDO: Copied libssl for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libssl for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pyenc):
        xbmcvfs.delete(pyenc)
    fyenc = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_yenc.so.' + parch)
    xbmcvfs.copy(fyenc, pyenc)
    xbmc.log('AUDO: Copied _yenc.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _yenc.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(ppar2):
        xbmcvfs.delete(ppar2)
    fpar2 = xbmc.translatePath(__dependencies__ + '/lib/multiarch/par2.' + parch)
    xbmcvfs.copy(fpar2, ppar2)
    os.chmod(ppar2, 0755)
    xbmc.log('AUDO: Copied par2 for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying par2 for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(punrar):
        xbmcvfs.delete(punrar)
    funrar = xbmc.translatePath(__dependencies__ + '/lib/multiarch/unrar.' + parch)
    xbmcvfs.copy(funrar, punrar)
    os.chmod(punrar, 0755)
    xbmc.log('AUDO: Copied unrar for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying unrar for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p7za):
        xbmcvfs.delete(p7za)
    f7za = xbmc.translatePath(__dependencies__ + '/lib/multiarch/7za.' + parch)
    xbmcvfs.copy(f7za, p7za)
    os.chmod(p7za, 0755)
    xbmc.log('AUDO: Copied 7za for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying 7za for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

xbmcvfs.File(xbmc.translatePath(__dependencies__ + '/arch.' + parch), 'w').close()
