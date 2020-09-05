from app.daos import bowler_dao

class bowlerService:
    def update_bowler(self, bowler_id, data -> dict):
        bowler = bowler_dao.get(bowler_id)
        # Update bowler with data        
        # check bowler for business logic
        # example: lowercase all emails
        return bowlerbowler_service = bowlerService()