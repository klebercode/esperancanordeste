# coding: utf-8

from django.core.urlresolvers import reverse_lazy

# from grappelli_extensions.nodes import CLNode


class Navbar(object):
    nodes = (
        ('Home', {'nodes': (
            ('Empresa', {
                'url': reverse_lazy(
                    'admin:core_enterprise_changelist'),
                'perm': 'core.change_enterprise',
            }),
            ('Box da Home', {
                'url': reverse_lazy(
                    'admin:core_step_changelist'),
                'perm': 'core.change_step',
            }),
            ('Apoio Social', {
                'url': reverse_lazy(
                    'admin:core_social_changelist'),
                'perm': 'core.change_social',
            }),
        )}),
        ('Institucional', {
            'url': reverse_lazy(
                'admin:core_institutional_changelist'),
            'perm': 'core.change_institutional',
        }),
        ('Campanhas', {
            'url': reverse_lazy(
                'admin:campain_entry_changelist'),
            'perm': 'campain.change_entry',
        }),
        ('Cotação', {
            'url': reverse_lazy(
                'admin:sale_estimate_changelist'),
            'perm': 'sale.change_estimate',
        }),
        ('Receba seu pedido', {
            'url': reverse_lazy(
                'admin:core_order_changelist'),
            'perm': 'core.change_order',
        }),
        ('Marcas', {'nodes': (
            ('Descrição da página', {
                'url': reverse_lazy(
                    'admin:core_brand_changelist'),
                'perm': 'core.change_brand',
            }),
            ('Marcas dos Parceiros', {
                'url': reverse_lazy(
                    'admin:core_partner_changelist'),
                'perm': 'core.change_partner',
            }),
        )}),
        ('Área de Atuação', {'nodes': (
            ('Descrição da página', {
                'url': reverse_lazy(
                    'admin:sale_area_changelist'),
                'perm': 'sale.change_area',
            }),
            ('Segmentos', {
                'url': reverse_lazy(
                    'admin:sale_segment_changelist'),
                'perm': 'sale.change_segment',
            }),
            ('Vendedores', {
                'url': reverse_lazy(
                    'admin:sale_seller_changelist'),
                'perm': 'sale.change_seller',
            }),
            ('Emails', {
                'url': reverse_lazy(
                    'admin:sale_email_changelist'),
                'perm': 'sale.change_email',
            }),
            ('Fones', {
                'url': reverse_lazy(
                    'admin:sale_phone_changelist'),
                'perm': 'sale.change_phone',
            }),
        )}),
        ('Catálogo', {'nodes': (
            ('Categorias', {
                'url': reverse_lazy(
                    'admin:catalog_category_changelist'),
                'perm': 'catalog.change_category',
            }),
            ('Produtos', {
                'url': reverse_lazy(
                    'admin:catalog_product_changelist'),
                'perm': 'catalog.change_product',
            }),
            ('Catálogo para Download', {
                'url': reverse_lazy(
                    'admin:catalog_catalog_changelist'),
                'perm': 'catalog.change_catalog',
            }),
        )}),
        ('Administração', {'nodes': (
            ('Usuários', {
                'url': reverse_lazy('admin:auth_user_changelist'),
                'perm': 'auth.change_user',
            }),
            ('Grupos', {
                'url': reverse_lazy('admin:auth_group_changelist'),
                'perm': 'auth.change_group',
            }),
        )}),
        # ('Sites',
        #     {'url': reverse_lazy('admin:sites_site_changelist')}),
        # ('Nodes', {'nodes': (
        #     CLNode('auth', 'user'),
        #     CLNode('sites', 'site'),
        # )}),
        # CLNode('auth', 'user', u"Site users"),
    )


class Sidebar(object):
    nodes = (
        ('Home', {'nodes': (
            ('Empresa', {
                'url': reverse_lazy(
                    'admin:core_enterprise_changelist'),
                'perm': 'core.change_enterprise',
            }),
            ('Box da Home', {
                'url': reverse_lazy(
                    'admin:core_step_changelist'),
                'perm': 'core.change_step',
            }),
            ('Apoio Social', {
                'url': reverse_lazy(
                    'admin:core_social_changelist'),
                'perm': 'core.change_social',
            }),
        )}),
        ('Institucional', {
            'url': reverse_lazy(
                'admin:core_institutional_changelist'),
            'perm': 'core.change_institutional',
        }),
        ('Campanhas', {
            'url': reverse_lazy(
                'admin:campain_entry_changelist'),
            'perm': 'campain.change_entry',
        }),
        ('Cotação', {
            'url': reverse_lazy(
                'admin:sale_estimate_changelist'),
            'perm': 'sale.change_estimate',
        }),
        ('Receba seu pedido', {
            'url': reverse_lazy(
                'admin:core_order_changelist'),
            'perm': 'core.change_order',
        }),
        ('Marcas', {'nodes': (
            ('Descrição da página', {
                'url': reverse_lazy(
                    'admin:core_brand_changelist'),
                'perm': 'core.change_brand',
            }),
            ('Marcas dos Parceiros', {
                'url': reverse_lazy(
                    'admin:core_partner_changelist'),
                'perm': 'core.change_partner',
            }),
        )}),
        ('Área de Atuação', {'nodes': (
            ('Descrição da página', {
                'url': reverse_lazy(
                    'admin:sale_area_changelist'),
                'perm': 'sale.change_area',
            }),
            ('Segmentos', {
                'url': reverse_lazy(
                    'admin:sale_segment_changelist'),
                'perm': 'sale.change_segment',
            }),
            ('Vendedores', {
                'url': reverse_lazy(
                    'admin:sale_seller_changelist'),
                'perm': 'sale.change_seller',
            }),
            ('Emails', {
                'url': reverse_lazy(
                    'admin:sale_email_changelist'),
                'perm': 'sale.change_email',
            }),
            ('Fones', {
                'url': reverse_lazy(
                    'admin:sale_phone_changelist'),
                'perm': 'sale.change_phone',
            }),
        )}),
        ('Catálogo', {'nodes': (
            ('Categorias', {
                'url': reverse_lazy(
                    'admin:catalog_category_changelist'),
                'perm': 'catalog.change_category',
            }),
            ('Produtos', {
                'url': reverse_lazy(
                    'admin:catalog_product_changelist'),
                'perm': 'catalog.change_product',
            }),
            ('Catálogo para Download', {
                'url': reverse_lazy(
                    'admin:catalog_catalog_changelist'),
                'perm': 'catalog.change_catalog',
            }),
        )}),
        ('Administração', {'nodes': (
            ('Usuários', {
                'url': reverse_lazy('admin:auth_user_changelist'),
                'perm': 'auth.change_user',
            }),
            ('Grupos', {
                'url': reverse_lazy('admin:auth_group_changelist'),
                'perm': 'auth.change_group',
            }),
        )}),
        # ('Sites',
        #     {'url': reverse_lazy('admin:sites_site_changelist')}),
        # ('Nodes', {'nodes': (
        #     CLNode('auth', 'user'),
        #     CLNode('sites', 'site'),
        # )}),
        # CLNode('auth', 'user', u"Site users"),
    )
