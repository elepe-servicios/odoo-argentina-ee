import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """
    Elimina la vista res_config_settings_view_form si existe en la instancia.
    Esta vista fue eliminada del módulo y debe removerse de la base de datos.
    """
    # Verificar si la vista existe consultando ir_model_data
    cr.execute("""
        SELECT imd.id, imd.res_id
        FROM ir_model_data imd
        WHERE imd.module = 'account_accountant_ux'
          AND imd.name = 'res_config_settings_view_form'
          AND imd.model = 'ir.ui.view'
    """)
    result = cr.fetchone()

    if result:
        xmlid_id, view_id = result
        _logger.info(
            "Eliminando vista account_accountant_ux.res_config_settings_view_form "
            "(ir.model.data id=%s, ir.ui.view id=%s)", xmlid_id, view_id
        )

        # Eliminar vistas heredadas (hijas) de esta vista
        cr.execute("""
            DELETE FROM ir_ui_view
            WHERE inherit_id = %s
        """, (view_id,))
        deleted_children = cr.rowcount
        if deleted_children:
            _logger.info("Eliminadas %s vistas heredadas", deleted_children)

        # Eliminar la vista principal
        cr.execute("""
            DELETE FROM ir_ui_view
            WHERE id = %s
        """, (view_id,))

        # Eliminar el registro de ir_model_data
        cr.execute("""
            DELETE FROM ir_model_data
            WHERE id = %s
        """, (xmlid_id,))

        _logger.info("Vista eliminada correctamente")
    else:
        _logger.info(
            "La vista account_accountant_ux.res_config_settings_view_form no existe, "
            "no es necesario eliminarla"
        )
