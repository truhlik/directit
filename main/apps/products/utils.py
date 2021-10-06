def product_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<id>/<filename>
    return 'product_{0}/{1}'.format(instance.id, filename)
