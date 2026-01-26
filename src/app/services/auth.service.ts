import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly COOKIE_NAME = 'user_session';
  private loggedIn = false;

  constructor(private cookieService: CookieService) {
    this.loggedIn = this.cookieService.check(this.COOKIE_NAME);
  }

  login(): void {
    this.cookieService.set(this.COOKIE_NAME, 'true', { expires: 7, path: '/' });
    this.loggedIn = true;
  }

  logout(): void {
    this.cookieService.delete(this.COOKIE_NAME, '/');
    this.loggedIn = false;
  }

  isAuthenticated(): boolean {
    return this.loggedIn;
  }
}
