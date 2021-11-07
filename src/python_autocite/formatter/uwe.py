from python_autocite.formatter import CitationFormatter

class UWEHarvardFormatter(CitationFormatter):

    def format(self, citation):
        format = self._get_format()

        return format % (
            self._assemble_authors(citation.authors),
            self._format_pubdate(citation.publication_date),
            citation.title,
            citation.url,
            self._format_accessdate(citation.access_date)
            )

    def _get_format(self):
        return "%s (%s) \x1B[3m%s\x1B[0m. Available from: %s [Accessed %s]."

    def _get_author_format(self, authors):
        if (len(authors) == 0):
            return self.AUTHOR_UNKNOWN
        elif (len(authors) == 1):
            return "%s"
        elif (len(authors) == 2):
            return "%s, & %s"
        else:
            format_string = "%s, " * (len(authors)-1)
            return format_string + "& %s"

    def _assemble_authors(self, authors):

        formatted_names = set()

        for a in authors:
            first_last = a.split()
            if (len(first_last) > 1):
                # This pulls the last name and first initial
                formatted_names.add(first_last[1] + ", " + first_last[0][0] + ".")

        authors = list(formatted_names)
        if (len(authors) < 1):
            return self.AUTHOR_UNKNOWN

        authors.sort()

        formatted_authors = self._get_author_format(authors) % tuple(authors)
        return formatted_authors

    def _format_pubdate(self, date):
        if (date is not None):
            return date.strftime("%Y")
        else:
            return self.PUBDATE_UNKNOWN

    def _format_accessdate(self, date):
        if (date is not None):
            return date.strftime("%s %B %Y")
        else:
            return self.ACCESSDATE_UNKNOWN