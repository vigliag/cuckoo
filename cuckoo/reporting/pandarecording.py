# Copyright (C) 2012-2013 Claudio Guarnieri.
# Copyright (C) 2014-2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import calendar
import datetime
import os
import shutil
from cuckoo.common.abstracts import Report
from cuckoo.common.exceptions import CuckooReportError


class Pandarecording(Report):
    """Saves analysis results in JSON format."""

    def run(self, results):
        """Writes report.
        @param results: Cuckoo results dict.
        @raise CuckooReportError: if fails to write report.
        """
        print("moving panda recording")

        try:
            workdir = os.getcwd()
            target = self.analysis_path
            files = ["sysrec-rr-nondet.log", "sysrec-rr-snp", "events.txt", "pids.txt" ]
            for file in files:
                shutil.move(os.path.join(workdir, file ), target)

        except (TypeError, IOError) as e:
            raise CuckooReportError("Failed to move sysrec files: %s" % e)