# -*- coding: utf-8 -*-

"""
This file is part of zoteromarkdown.

zoteromarkdown is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

zoteromarkdown is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with zoteromarkdown.  If not, see <http://www.gnu.org/licenses/>.
"""

from academicmarkdown import YAMLParser
import os

class IncludeParser(YAMLParser):
	
	"""
	Interprets bash commands in YAML blocks of this type:
	
	%--	exec: "date +'Updated: %x'" --%
	"""
	
	def __init__(self, verbose=False):
		
		"""See YAMLParser.__init__()."""
		
		super(IncludeParser, self).__init__(_object=u'include', verbose=verbose)
	
	def parseObject(self, md, _yaml, d):
		
		"""See YAMLParser.parseObject()."""
		
		if not isinstance(d, basestring):
			return u'Expecting a string, not "%s"' % d
		d = self.getPath(d)
		self.msg('Include: %s' % d)
		_md = open(d).read().decode(u'utf-8')
		ip = IncludeParser(verbose=self.verbose)
		_md = ip.parse(_md)
		return md.replace(_yaml, _md)
	