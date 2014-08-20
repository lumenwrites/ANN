(import [django.db [models]])
(import [django.contrib.auth.models [User]])
(import [django.core.urlresolvers [reverse]])
(import [django.template.defaultfilters [slugify]])


(defclass Point [models.Model]
  [[posX (models.IntegerField)]])
