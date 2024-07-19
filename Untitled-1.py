
Traceback (most recent call last):
  File "/home/odoo/src/odoo/odoo/models.py", line 5849, in ensure_one
    _id, = self._ids
ValueError: too many values to unpack (expected 1)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/odoo/src/odoo/odoo/http.py", line 1764, in _serve_db
    return service_model.retrying(self._serve_ir_http, self.env)
  File "/home/odoo/src/odoo/odoo/service/model.py", line 133, in retrying
    result = func()
  File "/home/odoo/src/odoo/odoo/http.py", line 1791, in _serve_ir_http
    response = self.dispatcher.dispatch(rule.endpoint, args)
  File "/home/odoo/src/odoo/odoo/http.py", line 1995, in dispatch
    result = self.request.registry['ir.http']._dispatch(endpoint)
  File "/home/odoo/src/odoo/addons/website/models/ir_http.py", line 235, in _dispatch
    response = super()._dispatch(endpoint)
  File "/home/odoo/src/odoo/odoo/addons/base/models/ir_http.py", line 222, in _dispatch
    result = endpoint(**request.params)
  File "/home/odoo/src/odoo/odoo/http.py", line 741, in route_wrapper
    result = endpoint(self, *args, **params_ok)
  File "/home/odoo/src/odoo/addons/web/controllers/dataset.py", line 24, in call_kw
    return self._call_kw(model, method, args, kwargs)
  File "/home/odoo/src/odoo/addons/web/controllers/dataset.py", line 20, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
  File "/home/odoo/src/odoo/odoo/api.py", line 464, in call_kw
    result = _call_kw_model(method, model, args, kwargs)
  File "/home/odoo/src/odoo/odoo/api.py", line 435, in _call_kw_model
    result = method(recs, *args, **kwargs)
  File "/home/odoo/src/odoo/addons/web/models/models.py", line 47, in web_search_read
    values_records = records.web_read(specification)
  File "/home/odoo/src/odoo/addons/web/models/models.py", line 86, in web_read
    values_list: List[Dict] = self.read(fields_to_read, load=None)
  File "/home/odoo/src/odoo/odoo/models.py", line 3540, in read
    return self._read_format(fnames=fields, load=load)
  File "/home/odoo/src/odoo/odoo/models.py", line 3751, in _read_format
    vals[name] = convert(record[name], record, use_display_name)
  File "/home/odoo/src/odoo/odoo/models.py", line 6631, in __getitem__
    return self._fields[key].__get__(self, self.env.registry[self._name])
  File "/home/odoo/src/odoo/odoo/fields.py", line 1207, in __get__
    self.compute_value(recs)
  File "/home/odoo/src/odoo/odoo/fields.py", line 1389, in compute_value
    records._compute_field_value(self)
  File "/home/odoo/src/odoo/addons/mail/models/mail_thread.py", line 424, in _compute_field_value
    return super()._compute_field_value(field)
  File "/home/odoo/src/odoo/odoo/models.py", line 4875, in _compute_field_value
    fields.determine(field.compute, self)
  File "/home/odoo/src/odoo/odoo/fields.py", line 102, in determine
    return needle(*args)
  File "/home/odoo/src/user/school_reg_base/models/promissory_model.py", line 264, in amount_to_words2
    calculation_method = self.calculation_method
  File "/home/odoo/src/odoo/odoo/fields.py", line 1148, in __get__
    record.ensure_one()
  File "/home/odoo/src/odoo/odoo/models.py", line 5852, in ensure_one
    raise ValueError("Expected singleton: %s" % self)
ValueError: Expected singleton: promissory.note(17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

The above server error caused the following client error


Create the following tables and their CRUD pages in the backend:





Section [id, section, slug, icon, logo, status, created_date, modified_date, deleted_date]
Department [id, department, slug, icon, logo, status, created_date, modified_date, deleted_date]
Category [id, category, slug, icon, logo, status, created_date, modified_date, deleted_date]
Category [id, category, slug, icon, logo, status, created_date, modified_date, deleted_date]
Sub Category [id, sub_category, slug, logo, icon, status, category_id, created_date, modified_date, deleted_date]
Source [id, source, slug, icon, logo, status, created_date, modified_date, deleted_date]
Reference [id, reference, slug, icon, link, status, created_date, modified_date, deleted_date]
Writer [id, writer, slug, icon, image, status, created_date, modified_date, deleted_date]
Location [id, location, status, created_date, modified_date, deleted_date]
Module [id, module, slug, ison, logo, status, created_date, modified_date, deleted_date]


