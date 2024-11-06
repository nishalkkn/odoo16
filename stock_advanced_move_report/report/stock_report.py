# -*- coding: utf-8 -*-
from odoo import models, api


class HrAttendanceReport(models.AbstractModel):
    _name = "report.stock_advanced_move_report.stock_report"
    _description = "Stock Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """function for get pdf report values"""
        query = """select 
                stock_move.date as date,
                product_template.name as product,
                stock_move.state as status,
                stock_location.complete_name as from_location,
                stock_move.location_dest_id as destination_location
                from stock_move
                inner join stock_location on stock_location.id = stock_move.location_id"""
        self._cr.execute(query)
        report = self._cr.dictfetchall()
        return {
            'report': report,
        }

# hr_employee.name  as employee,
#                     hr_employee.work_email  as email,
#                     hr_department.complete_name  as department,
#                     TO_CHAR(hr_attendance.check_in, 'HH24:MM:SS') as check_in,
#                     TO_CHAR(hr_attendance.check_out, 'HH24:MM:SS') as check_out,
#                     DATE(hr_attendance.check_in) as date,
#                     ROUND(CAST(hr_attendance.worked_hours AS numeric),2)  as worked_hours,
#                     ROUND(CAST(hr_attendance.overtime_hours AS numeric),2) as overtime_hours
#                     from hr_attendance
#                     inner join hr_employee on hr_employee.id = hr_attendance.employee_id
#                     inner join hr_department on hr_employee.department_id = hr_department.id
#                     where True"""
