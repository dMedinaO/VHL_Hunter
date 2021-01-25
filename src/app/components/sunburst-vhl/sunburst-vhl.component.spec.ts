import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SunburstVHLComponent } from './sunburst-vhl.component';

describe('SunburstVHLComponent', () => {
  let component: SunburstVHLComponent;
  let fixture: ComponentFixture<SunburstVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SunburstVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SunburstVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
