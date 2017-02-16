import cherrypy
import marbaloo_schedule

schedule_plugin = marbaloo_schedule.Plugin(cherrypy.engine)
schedule_plugin.subscribe()
cherrypy.tools.schedule = marbaloo_schedule.Tool()


class Root(object):
    job_started = False

    def do_jobs(self):
        import schedule
        # request level jobs
        # e.g: send emails
        # if my_job_completed:
        #     schedule.CancelJob
        pass

    @cherrypy.expose
    def index(self):
        schedule = cherrypy.request.schedule
        if self.job_started is False:
            schedule.every(5).seconds.do(self.do_jobs)
            return 'jobs started :)'
        else:
            return 'jobs already started!'

config = {
    '/': {
        'tools.schedule.on': True
    }
}
cherrypy.quickstart(Root(), '/', config)








################3
import cherrypy
import marbaloo_schedule

schedule_plugin = marbaloo_schedule.Plugin(cherrypy.engine)
schedule_plugin.subscribe()


class Root:
    pass

cherrypy.tree.mount(Root(), '/', {})
cherrypy.engine.signals.subscribe()
cherrypy.engine.start()


def do_server_jobs():
    # server level jobs
    print('Job is Done')
    pass
schedule_plugin.schedule.every(5).seconds.do(do_server_jobs)

cherrypy.engine.block()
